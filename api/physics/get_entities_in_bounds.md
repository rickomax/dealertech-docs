---
layout: default
title: "physics.get_entities_in_bounds(mins, maxs, debug) -> table"
parent: physics
grand_parent: API Reference
nav_order: 1
---

# `physics.get_entities_in_bounds(mins, maxs, debug) -> table`

Returns the entities whose colliders overlap an axis-aligned bounding volume.

**Parameters**
- `mins` (`vector`) — Minimum corner in world coordinates
- `maxs` (`vector`) — Maximum corner in world coordinates
- `debug` (`boolean`, default `false`) — When `true`, draws a debug wireframe of the volume

**Returns**
- `table` — A 1-indexed table where each value is the Lua instance table of an entity intersecting the volume.

