---
layout: default
title: ui_image
parent: API Reference
---

# `ui_image`

`ui_image` is a UI image element that renders a texture loaded from the engine resources.

`ui_image` inherits from [`ui_element`](ui_element.md): `set_position`, `set_selectable`, `destroy`, `center_on_x`, `rebuild`.

---

## Creation

### `ui_image.create(panel) -> ui_image`
Creates a new image element and adds it to the given panel.

**Parameters**
- `panel` (`ui_panel`) — Parent panel.

**Returns**
- `ui_image`

You can also call the namespace directly:

```lua
local img = ui_image(panel)
```

---

## Functions

### `ui_image:set_image(filename)`
Sets the image texture from a resource filename.

**Parameters**
- `filename` (`string`) — Texture filename.

**Errors**
- Throws if the texture cannot be found.

---

### `ui_image:set_size(width, height)`
Sets the rendered size of the image, in UI units.

**Parameters**
- `width` (`number`) — Width in UI units.
- `height` (`number`) — Height in UI units.

---

### `ui_image:set_color(color)`
Sets the image tint colour.

**Parameters**
- `color` (`vector4`) — Tint colour as RGBA in `[0, 1]`.

---

### `ui_image:set_native_size()`
Resizes the image to match the source texture's native pixel size.

---

## Example

```lua
local panel = ui_panel.create()

local crosshair = ui_image.create(panel)
crosshair:set_image("hud/crosshair.png")
crosshair:set_native_size()
crosshair:set_color(vector4.create(1, 1, 1, 0.8))
crosshair:center_on_x()
```
