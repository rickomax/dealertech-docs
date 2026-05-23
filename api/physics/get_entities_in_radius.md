---
layout: default
title: "`physics.get_entities_in_radius(origin, radius, debug) -> table`"
parent: physics
grand_parent: API Reference
nav_order: 2
---

# `physics.get_entities_in_radius(origin, radius, debug) -> table`

Returns the entities whose colliders overlap a sphere.

**Parameters**
- `origin` (`vector`) — Sphere center in world coordinates
- `radius` (`number`) — Sphere radius
- `debug` (`boolean`, default `false`) — When `true`, draws a debug wireframe of the sphere

**Returns**
- `table` — A 1-indexed table where each value is the Lua instance table of an entity intersecting the sphere.

---
