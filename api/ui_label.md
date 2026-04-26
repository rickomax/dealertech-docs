---
layout: default
title: ui_label
parent: API Reference
---
# `ui_label`

`ui_label` is a UI text element backed by TextMeshPro.
It auto-fits to the size of its text content.

`ui_label` inherits from [`ui_element`](ui_element.md): `set_position`, `set_selectable`, `destroy`, `center_on_x`, `rebuild`.

---

## Creation

### `ui_label.create(panel) -> ui_label`
Creates a new label and adds it to the given panel.

**Parameters**
- `panel` (`ui_panel`) — Parent panel.

**Returns**
- `ui_label`

---

## Functions

### `ui_label:set_font(font)`
Sets the font used to render the text.

**Parameters**
- `font` (`font`) — The font to apply.

---

### `ui_label:set_size(size)`
Sets the font size used to render the text.

**Parameters**
- `size` (`number`) — Font size in UI units.

---

### `ui_label:set_color(color)`
Sets the text colour.

**Parameters**
- `color` (`vector4`) — Colour as RGBA in `[0, 1]`.

---

### `ui_label:set_text(text)`
Sets the displayed text.

**Parameters**
- `text` (`string`) — Text to display.
