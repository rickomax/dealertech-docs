---
layout: default
title: physics
parent: API Reference
---
# `physics`

`physics` provides Lua-exposed physics queries and trace operations.

The trace functions return a `trace_result` object describing the first hit (if any), including impact normal, end position, traveled distance and the hit entity's instance table.

The overlap functions return an `array` of entity instance tables found inside a volume.

---

## Functions

### `physics.get_entities_in_bounds(mins, maxs) -> array`

Returns the entities found inside an axis-aligned bounding box.

**Parameters**
- `mins` (`vector`) — Minimum corner in world coordinates
- `maxs` (`vector`) — Maximum corner in world coordinates

**Returns**
- `array` — Each element is the Lua instance table of an entity whose collider intersects the volume.

**Notes**
- The returned array is reused between calls. Copy the values you need before calling another `physics` function.

---

### `physics.get_entities_in_radius(origin, radius) -> array`

Returns the entities found inside a sphere.

**Parameters**
- `origin` (`vector`) — Sphere center in world coordinates
- `radius` (`number`) — Sphere radius

**Returns**
- `array` — Each element is the Lua instance table of an entity whose collider intersects the sphere.

**Notes**
- The returned array is reused between calls. Copy the values you need before calling another `physics` function.

---

### `physics.trace_hull(start, end, mins, maxs, collisionType, ignore, debug) -> trace_result`

Traces a moving axis-aligned hull (box) from `start` to `end` and returns the first collision hit, if any.

This is typically used for character / entity movement where the object has volume.

**Parameters**
- `start` (`vector`) — Trace start position
- `end` (`vector`) — Trace end position
- `mins` (`vector`) — Hull minimum bounds (local-space)
- `maxs` (`vector`) — Hull maximum bounds (local-space)
- `collisionType` (`integer`) — Collision mask selector
  - `0` (default): trace against all solid collisions
  - `1`: trace against BSP solids only
- `ignore` (`entity|nil`) — Entity to ignore during the trace (commonly the caller)
- `debug` (`boolean`) — If `true`, draws debug visualization for the trace

**Returns**
- `trace_result` — A result object containing hit info.

**Result fields written**
- `start_solid` (`boolean`) — `true` if the start point is inside a blocking volume
- `fraction` (`number`) — How far the trace traveled, normalized to `[0, 1]`
- `end_position` (`vector`) — End position reached (hit point or final end)
- `normal` (`vector`) — Surface normal at the impact point (zero vector if no hit)
- `distance` (`number`) — World distance traveled before impact
- `hit_table` (`table|nil`) — Lua instance table of the hit entity (when the hit collider belongs to an entity)

---

### `physics.trace_line(start, end, collisionType, ignore, debug) -> trace_result`

Traces a line segment from `start` to `end` and returns the first collision hit, if any.

This is typically used for hitscan, visibility checks, or simple probes.

**Parameters**
- `start` (`vector`) — Trace start position
- `end` (`vector`) — Trace end position
- `collisionType` (`integer`) — Collision mask selector
  - `0` (default): trace against all solid collisions
  - `1`: trace against BSP solids only
- `ignore` (`entity|nil`) — Entity to ignore during the trace
- `debug` (`boolean`) — If `true`, draws debug visualization for the trace

**Returns**
- `trace_result` — A result object containing hit info.

**Result fields written**
- `fraction` (`number`)
- `end_position` (`vector`)
- `normal` (`vector`)
- `distance` (`number`)
- `hit_table` (`table|nil`)
