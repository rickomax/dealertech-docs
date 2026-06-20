---
layout: default
title: "entity:lock_axis(x, y, z)"
parent: entity
grand_parent: API Reference
nav_order: 63
---

# `entity:lock_axis(x, y, z)`

Locks or unlocks the entity rotation around each axis. While the move type is `move_type.physics`, the entity rotation is driven by the physics simulation and respects any locked axis.

**Parameters**
- `x` (`boolean`) — Whether to lock rotation around the X axis.
- `y` (`boolean`) — Whether to lock rotation around the Y axis.
- `z` (`boolean`) — Whether to lock rotation around the Z axis.

**Notes**
- Has no effect unless the entity move type is `move_type.physics`.
