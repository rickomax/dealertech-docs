---
layout: default
title: light_source
parent: API Reference
---
# `light_source`

`light_source` represents a networked dynamic light spawned at runtime, and also
provides BSP light style helpers used by maps with animated lights.

Each light instance synchronizes its position, colour, intensity and radius
across clients. Lights are created through `light_source.create` rather than
constructed directly.

Most static functions are server-authoritative — calling them on a non-server
instance has no effect.

---

## Creation

### `light_source.create(position, color, intensity, radius, is_static, parent) -> light_source|nil`
Spawns a networked dynamic light, optionally parented to an entity.

**Parameters**
- `position` (`vector`) — World position of the light.
- `color` (`vector`) — RGB colour with each component in the range `[0, 1]`.
- `intensity` (`number`) — Light intensity.
- `radius` (`number`) — Light range/radius.
- `is_static` (`boolean`) — When `true`, the light affects only the static lighting layer.
- `parent` (`entity|nil`) — Optional entity to parent the light to.

**Returns**
- `light_source|nil` — The spawned light, or `nil` if not running on the server.

**Server-only**
- Returns `nil` when not running on the server.

---

The `light_source` table is also callable directly with the same arguments as
`light_source.create`, so the following two calls are equivalent:

```lua
local l1 = light_source.create(pos, color, 1.0, 256, false)
local l2 = light_source(pos, color, 1.0, 256, false)
```

---

## BSP Light Styles

### `light_source.get_computed_style(index) -> number`
Returns the current computed brightness for a BSP light style index.

**Parameters**
- `index` (`integer`) — The light style index.

**Returns**
- `number` — The computed brightness, or `0` if not running on the server.

---

### `light_source.set_style(index, style)`
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

### `light_source:set_intensity(value)`
Sets the light intensity.

**Parameters**
- `value` (`number`) — The new intensity value.

**Server-only**
- Has no effect when not running on the server.
