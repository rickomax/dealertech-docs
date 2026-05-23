---
layout: default
title: "entity:move(velocity, angles)"
parent: entity
grand_parent: API Reference
nav_order: 27
---

# `entity:move(velocity, angles)`

Moves the entity by the given velocity for one simulation step, and updates its angles.

**Parameters**
- `velocity` (`vector`) — Velocity to apply.
- `angles` (`vector|nil`, default `nil`) — Optional new angles. If omitted, the current angles are kept.

**Notes**
- Has no effect when not running on the server.
- Has no effect if the entity move type is `move_type.none` or velocity is zero.
- For BSP-solid entities, the angles input is ignored.

