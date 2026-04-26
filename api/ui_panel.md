---
layout: default
title: ui_panel
parent: API Reference
---

# `ui_panel`

`ui_panel` is a UI container element that holds child UI elements (`ui_label`, `ui_image`, `ui_input_field`, or other `ui_panel`s).

A panel can be plain or scrollable. Scrollable panels are sized to the engine's reference resolution of `320 × 240` and provide auto-hiding horizontal/vertical scrollbars.

`ui_panel` inherits from [`ui_element`](ui_element.md): `set_position`, `set_selectable`, `destroy`, `center_on_x`, `rebuild`.

---

## Creation

### `ui_panel.create(parent, scrollable) -> ui_panel`
Creates a new UI panel.

**Parameters**
- `parent` (`ui_panel|nil`, default `nil`) — Optional parent panel. If omitted, the panel is added to the canvas root.
- `scrollable` (`boolean`, default `false`) — When `true`, creates the panel with a viewport, content container and auto-hiding scrollbars.

**Returns**
- `ui_panel`

You can also call the namespace directly:

```lua
local p = ui_panel(parent, true)
```

---

## Behavior

- Plain panels resize themselves to wrap their children when `rebuild()` is called.
- Scrollable panels keep their outer size at `320 × 240` and grow their inner content container to wrap children.

---

## Example

```lua
local root = ui_panel.create()
root:set_position(10, 10)

local label = ui_label.create(root)
label:set_text("Hello")

local list = ui_panel.create(root, true)   -- scrollable child panel
for i = 1, 30 do
    local row = ui_label.create(list)
    row:set_text("Item " .. i)
    row:set_position(0, (i - 1) * 16)
end

root:rebuild()
```
