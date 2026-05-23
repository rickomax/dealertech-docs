---
layout: default
title: ui_panel
parent: API Reference
has_children: true
nav_order: 28
---

# `ui_panel`

`ui_panel` is a UI container element that holds child UI elements (`ui_label`, `ui_image`, `ui_input_field`, or other `ui_panel`s).

A panel can be plain or scrollable. Scrollable panels are sized to the engine's reference resolution of `320 × 240` and provide auto-hiding horizontal/vertical scrollbars.

`ui_panel` inherits from [`ui_element`](ui_element.md): `set_position`, `set_selectable`, `destroy`, `center_on_x`, `rebuild`.
