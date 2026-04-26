---
layout: default
title: lights
parent: API Reference
---
# `lights`

`lights` provides Lua-exposed dynamic light spawning and BSP light style control.

All functions are static and accessed directly from the `lights` table.

Most functions only have an effect when called on the server.

---

## Functions

### `lights.get_computed_style(index) -> number`
Returns the current computed brightness for a BSP light style index.

**Parameters**
- `index` (`integer`) — The light style index.

**Returns**
- `number` — The computed brightness, or `0` if not running on the server.

---

### `lights.set_style(index, style)`
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

### `lights.create_light(position, color, intensity, radius, is_static, parent) -> light|nil`
Spawns a networked dynamic light.

**Parameters**
- `position` (`vector`) — World position of the light.
- `color` (`vector`) — RGB colour with each component in the range `[0, 1]`.
- `intensity` (`number`) — Light intensity.
- `radius` (`number`) — Light range/radius.
- `is_static` (`boolean`) — When `true`, the light affects only the static lighting layer.
- `parent` (`entity|nil`) — Optional entity to parent the light to.

**Returns**
- `light|nil` — The spawned light, or `nil` if not running on the server.
