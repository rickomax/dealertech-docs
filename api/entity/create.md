---
layout: default
title: "entity.create(className, origin, angles) -> table"
parent: entity
grand_parent: API Reference
nav_order: 5
---

# `entity.create(className, origin, angles) -> table`

Spawns a new entity with the given class name and returns its Lua instance table.

**Parameters**
- `className` (`string`) — The entity class name.
- `origin` (`vector|nil`, default zero vector) — Initial world position.
- `angles` (`vector|nil`, default zero vector) — Initial pitch, yaw and roll angles.

**Returns**
- `table` — Lua instance table of the spawned entity, or `nil` if not running on the server.

