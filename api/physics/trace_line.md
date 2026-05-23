---
layout: default
title: "`physics.trace_line(start, end, collisionType, ignore, debug) -> trace_result`"
parent: physics
grand_parent: API Reference
nav_order: 4
---

# `physics.trace_line(start, end, collisionType, ignore, debug) -> trace_result`

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
