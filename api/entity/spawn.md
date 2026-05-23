---
layout: default
title: "entity:spawn(delay)"
parent: entity
grand_parent: API Reference
nav_order: 6
---

# `entity:spawn(delay)`

Spawns this entity on the network, optionally after a delay.

**Parameters**
- `delay` (`number|nil`, default `0`) — Delay in seconds before spawn. `0` or negative spawns immediately.

**Returns**
- `boolean` — `true` if a delayed spawn was scheduled, `false` if spawned immediately or the call was ignored.

**Server-only**
- Has no effect when not running on the server.

