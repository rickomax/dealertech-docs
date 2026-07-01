---
layout: default
title: "entity:set_rest_speed(speed)"
parent: entity
grand_parent: API Reference
nav_order: 65
---

# `entity:set_rest_speed(speed)`

Sets the speed below which the entity comes to rest when it settles on a floor. When the entity is supported by a surface and its speed drops below this value it snaps to a complete stop instead of continuing to bounce.

**Parameters**
- `speed` (`number`) — Rest speed threshold. A value of `0` disables the behaviour. Defaults to `0`.

**Notes**
- Has no effect unless the entity move type is `move_type.physics`.
