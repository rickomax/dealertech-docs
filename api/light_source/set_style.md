---
layout: default
title: "`light_source.set_style(index, style)`"
parent: light_source
grand_parent: API Reference
nav_order: 3
---

# `light_source.set_style(index, style)`

Sets the animation pattern for a BSP light style index.

The pattern string is a sequence of brightness levels, where:
- `'a'` is the darkest level
- `'z'` is the brightest level
- One character is consumed per tick, looping back to the start.

**Parameters**
- `index` (`integer`) — The light style index.
- `style` (`string`) — The animation pattern string.

**Server-only**
- Has no effect when not running on the server.

---

## Instance Functions
