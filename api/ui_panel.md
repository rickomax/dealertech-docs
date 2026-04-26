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

---

## Behavior

- Plain panels resize themselves to wrap their children when `rebuild()` is called.
- Scrollable panels keep their outer size at `320 × 240` and grow their inner content container to wrap children.
