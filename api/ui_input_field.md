---
layout: default
title: ui_input_field
parent: API Reference
---
# `ui_input_field`

`ui_input_field` is a UI text input element backed by a TextMeshPro input field.

It supports change/submit callbacks and multiple content types (integer, decimal, password, email, standard).

`ui_input_field` inherits from [`ui_element`](ui_element.md): `set_position`, `set_selectable`, `destroy`, `center_on_x`, `rebuild`.

---

## Creation

### `ui_input_field.create(panel) -> ui_input_field`
Creates a new input field element and adds it to the given panel.

**Parameters**
- `panel` (`ui_panel`) — Parent panel.

**Returns**
- `ui_input_field`

---

## Functions

### `ui_input_field:set_font(font)`
Sets the font used for the text and placeholder.

**Parameters**
- `font` (`font`) — The font to apply.

---

### `ui_input_field:set_size(size)`
Sets the font size for the text and placeholder.

**Parameters**
- `size` (`number`) — Font size in UI units.

---

### `ui_input_field:set_color(color)`
Sets the text colour.

**Parameters**
- `color` (`vector4`) — Colour as RGBA in `[0, 1]`.

---

### `ui_input_field:set_text(text)`
Sets the current text value.

**Parameters**
- `text` (`string`) — New text content.

---

### `ui_input_field:get_text() -> string`
Returns the current text value.

---

### `ui_input_field:set_content_type(content_type)`
Sets the content validation mode for the input field.

**Parameters**
- `content_type` (`string`) — One of:
  - `"integer"`
  - `"decimal"`
  - `"password"`
  - `"email"`
  - any other value defaults to `"standard"`

---

### `ui_input_field:set_char_limit(limit)`
Sets the maximum number of characters allowed in the input field.

**Parameters**
- `limit` (`integer`) — Character limit. Use `0` for no limit.

---

### `ui_input_field:on_change(callback)`
Registers a callback invoked every time the text value changes.

Replaces any previously registered change listener.

**Parameters**
- `callback` (`function`) — Lua function invoked with the new text value as its argument.

---

### `ui_input_field:on_submit(callback)`
Registers a callback invoked when the user submits the input (e.g. presses Enter).

Replaces any previously registered change listener.

**Parameters**
- `callback` (`function`) — Lua function invoked with the submitted text value as its argument.
