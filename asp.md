---
layout: default
title: ASP Template Format
nav_order: 5
---

# ASP Template Format

ASP is the XML/HTML-like markup language used to build user interfaces. An `.asp` file describes a tree of UI elements declaratively; at load time it is transpiled to Lua that constructs the corresponding `ui_panel`, `ui_label`, `ui_image` and `ui_input_field` elements.

ASP files live in `StreamingAssets/ui/` and are loaded from Lua with `load_ui`:

```lua
local root = ui_panel()
load_ui("menu.asp", root)
```

The name *ASP* comes from the `<% ... %>` code tags, which work like classic server-page templates: markup and embedded Lua are interleaved, and the whole document compiles to a single Lua chunk.

## How It Works

The transpiler scans the markup and emits Lua. The compiled chunk receives the parent passed to `load_ui` as a vararg bound to a local named `__parent`, and **returns the first top-level element** so the caller can keep a handle to it.

```
<image image="bg.png" native_size />
```

compiles to:

```lua
local __parent = ...
local v0 = ui_image(__parent)
v0:set_image("bg.png")
v0:set_native_size()
return v0
```

- Top-level elements are parented to `__parent`.
- Nested elements are parented to their enclosing element.
- Whitespace between tags is ignored.

## Elements

A tag `<name>` maps to a constructor call `ui_<name>(parent)`. The built-in element types are:

| Tag | Constructor | Element |
|:----|:------------|:--------|
| `<panel>` | `ui_panel(parent)` | A container that holds child elements. |
| `<label>` | `ui_label(parent)` | A text label. |
| `<image>` | `ui_image(parent)` | An image. |
| `<input_field>` | `ui_input_field(parent)` | A text input field. |

Elements may be self-closed (`<image ... />`) or contain children:

```
<panel ref="panel">
    <image image="crosshair.png" native_size />
    <label text="Ready" x="0" y="16" />
</panel>
```

## The `ref` Attribute

By default each element is assigned an auto-generated local (`v0`, `v1`, …), scoped to where it appears — inside a `<template>`, only to that builder function. Add `ref="name"` to bind it to a named handle that is shared across the **entire loaded asp**: every template builder and the trailing `<% %>` block can read or assign it.

```
<panel ref="panel" scrollable>
    <label ref="title" text="Main Menu" x="0" y="16" center_on_x />
</panel>
<% title:set_color(vector4(1, 1, 0, 1)) %>
```

Ref handles are **not** Lua globals. They are forward-declared as locals at the top of the generated chunk and captured as upvalues, so they stay invisible to other scripts and never touch the global table. Choosing ref names that don't collide is the author's responsibility — reusing a name (for example `ref="panel"` in several templates) shares one handle that is reassigned to whichever element was built most recently.

## Attributes

Each attribute compiles to a setter call on the element. By convention `attr="value"` becomes `:set_<attr>(value)`, and a valueless attribute (a *flag*) becomes `:set_<attr>()`:

```
<image image="sbar.png" native_size />
```
```lua
local v0 = ui_image(__parent)
v0:set_image("sbar.png")   -- image="sbar.png"
v0:set_native_size()       -- native_size (flag)
```

The set of usable attributes therefore matches the element's `set_*` methods — see the [API Reference](api/) for each element type. Commonly used attributes:

| Attribute | Example | Compiles to |
|:----------|:--------|:------------|
| `text` | `text="Score"` | `:set_text("Score")` |
| `font` | `font="<%= main_font %>"` | `:set_font(main_font)` |
| `image` | `image="face.png"` | `:set_image("face.png")` |
| `size` | `size="8"` | `:set_size(8)` |
| `x` | `x="112"` | `:set_x(112)` |
| `y` | `y="216"` | `:set_y(216)` |
| `native_size` | `native_size` | `:set_native_size()` |
| `center_on_x` | `center_on_x` | `:set_center_on_x()` |

Use `x` and `y` to position an element (`set_x` / `set_y`); the Y axis grows downward, matching screen-space coordinates.

### Attribute Values

How a value is compiled depends on its content:

- **String literal** — quoted as a Lua string: `text="new game"` → `:set_text("new game")`.
- **Bare number** — passed through unquoted: `size="8"` → `:set_size(8)`.
- **`<%= expr %>`** — treated as a Lua expression, inserted verbatim: `font="<%= main_font %>"` → `:set_font(main_font)`.

Because a plain literal is quoted, to pass a Lua **variable** or expression you must escape into Lua with `<%= %>` — `font="main_font"` would pass the *string* `"main_font"`, not the font object. The same applies to computed positions: `y="<%= (i + 1) * 10 %>"`.

### Special Attributes

A few attributes have dedicated handling instead of the `set_<attr>` convention:

| Attribute | Element | Compiles to |
|:----------|:--------|:------------|
| `scrollable` | `<panel>` | `ui_panel(parent, true)` — a flag consumed by the constructor, producing a scrollable panel with auto-managed scrollbars. |
| `on_select="..."` | any | `:set_on_select(function() ... end)` — the body becomes the click callback. |
| `on_submit="..."` | `<input_field>` | `:set_on_submit(function(value) ... end)` — `value` is the submitted text. |

```
<label text="quit" x="0" y="70" center_on_x on_select="quit_game()" />
```
```lua
local v0 = ui_label(__parent)
v0:set_text("quit")
v0:set_x(0)
v0:set_y(70)
v0:set_center_on_x()
v0:set_on_select(function()
    quit_game()
end)
```

## Element Text

Plain text written between an element's tags is **ignored**. Set text with the `text` attribute, or with an embedded expression:

```
<label text="Static label" />
<label><%= "Dynamic: " .. tostring(score) %></label>
```

A `<%= expr %>` between tags sets the enclosing element's text from the (unquoted) expression.

## Embedded Lua

Two tags let you mix Lua into the markup:

- **`<%= expr %>`** — an expression. Used as an attribute value or as element text (see above).
- **`<% code %>`** — raw statements, emitted inline at that point in the generated chunk. Use it for locals, loops, and any code that runs while the UI is built.

```
<panel ref="panel" scrollable>
    <% local maps = bsp.get_maps() %>
    <% for i = 1, #maps do %>
    <label text="<%= maps[i] %>" x="0" y="<%= i * 10 %>" center_on_x />
    <% end %>
</panel>
```

The `for` wraps the `<label>` element, so one label is created per map. Each iteration's loop variable is captured independently, so callbacks defined inside the loop close over the correct value.

## Reactive Bindings

When the **entire** value of an attribute (or an element's text) is `<%=# expr %>`, it compiles to a reactive *binding* instead of a one-shot set. The element re-derives that attribute from `expr` every tick and pushes the result through `set_<attr>`:

```
<label font="<%= main_font %>" text='<%=# "Time: " .. tostring(time) %>' x="0" y="88" center_on_x />
```
```lua
local v0 = ui_label(panel)
v0:set_font(main_font)
v0:add_binding(
    function() return "Time: " .. tostring(time) end,
    function(...) v0:set_text(...) end)
v0:set_x(0)
v0:set_y(88)
v0:set_center_on_x()
```

The getter is re-evaluated each tick; the setter is only called when the value actually changes. All getter results are forwarded, so multi-argument setters work if the getter returns multiple values.

You can also wire a binding manually with [`add_binding`](api/ui_element/add_binding.html):

```lua
label:add_binding(
    function() return get_score() end,
    function(value) label:set_text(value) end)
```

`add_binding(getter, setter)` registers a binding on the element; it is removed automatically when the element is destroyed.

> **Quoting:** the markup attribute delimiter and Lua strings both use quotes. Delimit the attribute with `'` to use double-quoted Lua strings inside (as above), or with `"` to use single-quoted Lua strings. The marker is `<%=#` with no space; `<%= #t %>` (with a space) is an ordinary length-operator expression.

## Templates

A `<template name="x">...</template>` block does **not** create elements where it appears. Instead it compiles to a global builder function `function x(__parent) ... end` that builds its contents into the panel you pass it and returns the root element. Calling the function (re)generates that subtree on demand:

```
<template name="main_menu">
    <panel ref="panel" scrollable>
        <label text="new game" x="0" y="16" center_on_x on_select="show(maps_menu)" />
        <label text="quit"     x="0" y="34" center_on_x on_select="quit_game()" />
    </panel>
</template>

<% show(main_menu) %>
```

Each template becomes a builder you can swap between to navigate screens. Because builders are global, refer to one before it is defined in the file — the call resolves at runtime. A common pattern keeps the *current* screen and rebuilds on demand:

```lua
<%
local current

function show(screen)
    if current then current:destroy() end
    current = screen(__parent)
    __parent:rebuild()
end
%>
```

## Comments

`<!-- ... -->` is a markup comment. Its contents are skipped entirely and not transpiled, so you can comment out elements and embedded code:

```
<!-- <label text="WIP" x="0" y="96" /> -->
```

## Loading from Lua

UI documents are loaded and unloaded through two global functions.

### `load_ui(file, parent)`

Loads `StreamingAssets/ui/<file>`, transpiles it, runs the resulting chunk with `parent` bound to `__parent`, and returns the root element (the first top-level element declared in the file).

**Parameters**
- `file` (`string`) — the file name under `StreamingAssets/ui/`, e.g. `"menu.asp"`.
- `parent` (`ui_element`, optional) — the element the document is built into; bound to `__parent`. When omitted, top-level elements attach to the canvas root.

**Returns** — the root `ui_element`. Raises an error if the file does not exist or the markup fails to compile (the error message includes the generated Lua).

### `unload_ui(...)`

Tears down a loaded UI.

A typical entry point creates a root container and loads a menu into it:

```lua
function load_main_menu()
    local root_panel = ui_panel()
    load_ui("menu.asp", root_panel)
    root_panel:rebuild()
end
```
