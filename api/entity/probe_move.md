---
layout: default
title: "entity:probe_move(angle, move_distance)"
parent: entity
grand_parent: API Reference
nav_order: 84
---

# `entity:probe_move(angle, move_distance)`

Tests whether the entity could step along a horizontal direction, without moving it.
Position and velocity are unchanged afterwards.

**Parameters**
- `angle` (`number`) - the yaw to test, in degrees; negative values fail the test
- `move_distance` (`number`) - the distance to cover

**Returns**
- `boolean` - whether the step would succeed

**Server-only** (returns `false` otherwise)
