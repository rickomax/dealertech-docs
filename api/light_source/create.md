---
layout: default
title: "light_source.create(position, color, intensity, radius, is_static, parent) -> light_source|nil"
parent: light_source
grand_parent: API Reference
nav_order: 1
---

# `light_source.create(position, color, intensity, radius, is_static, parent) -> light_source|nil`

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

