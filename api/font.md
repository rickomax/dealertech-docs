---
layout: default
title: font
parent: API Reference
---

# `font`

`font` represents a font asset loaded from a file in the engine `fonts` folder.

Font instances are passed to UI text elements such as `ui_label` and `ui_input_field` to control their appearance.

---

## Creation

### `font.create(filename) -> font`
Loads a font asset from the `fonts` folder.

**Parameters**
- `filename` (`string`) — The font filename relative to the `fonts` folder.

**Returns**
- `font`

**Errors**
- Throws if the font file cannot be found.

You can also call the namespace directly:

```lua
local f = font("default.ttf")
```

---

## Example

```lua
local f = font.create("default.ttf")

local panel = ui_panel.create()
local label = ui_label.create(panel)
label:set_font(f)
label:set_text("Hello, world!")
```
