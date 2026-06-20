---
layout: default
title: "entity:set_damping(damping)"
parent: entity
grand_parent: API Reference
nav_order: 64
---

# `entity:set_damping(damping)`

Sets the linear damping applied to the entity. Defaults to `0`.

**Parameters**
- `damping` (`number`) — The linear damping coefficient.

**Notes**
- Has no effect unless the entity move type is `move_type.physics`.
