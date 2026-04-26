---
layout: default
title: ui_element
parent: API Reference
---

# `ui_element`

`ui_element` is the base class shared by all UI elements exposed to Lua.

The following types inherit these members:
- `ui_panel`
- `ui_label`
- `ui_image`
- `ui_input_field`

You don't construct `ui_element` directly — call `create` on a derived type instead.

---

## Functions

### `ui_element:set_position(x, y)`
Sets the anchored position of this element.
The Y axis grows downward, matching screen-space coordinates.

**Parameters**
- `x` (`number`) — Horizontal position.
- `y` (`number`) — Vertical position (downward-positive).

---

### `ui_element:set_selectable(on_select, color)`
Marks this element as selectable and registers a callback for selection events.

**Parameters**
- `on_select` (`function`) — Lua function invoked when the element is selected.
- `color` (`vector4`) — Highlight/selected/pressed colour as RGBA in `[0, 1]`.

---

### `ui_element:destroy()`
Destroys this element and removes it from the scene.

---

### `ui_element:center_on_x()`
Centers this element horizontally inside the standard 320-unit reference width.

---

### `ui_element:rebuild()`
Forces an immediate layout rebuild of this element and its content.

Call after changing text or sizes if you depend on the new layout being applied immediately.

---

## Example

```lua
local panel = ui_panel.create()
local label = ui_label.create(panel)
label:set_text("Click me")
label:set_position(10, 20)
label:set_selectable(function()
    print("clicked")
end, vector4.create(1, 1, 0, 1))
panel:rebuild()
```
