---
layout: default
title: "entity:add_force_velocity(force)"
parent: entity
grand_parent: API Reference
nav_order: 29
---

# `entity:add_force_velocity(force)`

Applies an instantaneous velocity change to the entity's rigid body.

**Parameters**
- `force` (`vector`) — Velocity change to add, in world coordinates.

**Notes**
- Has no effect when not running on the server.
- Has no effect unless the entity move type is `move_type.physics`.

