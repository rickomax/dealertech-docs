---
layout: default
title: "`ui_panel.create(parent, scrollable) -> ui_panel`"
parent: ui_panel
grand_parent: API Reference
nav_order: 1
---

# `ui_panel.create(parent, scrollable) -> ui_panel`

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
