---
layout: default
title: "physics.trace_hull(start, end, mins, maxs, collisionType, ignore, debug) -> trace_result"
parent: physics
grand_parent: API Reference
nav_order: 3
---

# `physics.trace_hull(start, end, mins, maxs, collisionType, ignore, debug) -> trace_result`

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

