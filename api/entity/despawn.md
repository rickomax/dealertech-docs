---
layout: default
title: "`entity:despawn(delay)`"
parent: entity
grand_parent: API Reference
nav_order: 7
---

# `entity:despawn(delay)`

Despawns and removes the entity from the network, optionally after a delay.

**Parameters**
- `delay` (`number|nil`, default `0`) — Delay in seconds before despawn. `0` or negative despawns immediately.

**Returns**
- `boolean` — `true` if a delayed despawn was scheduled, `false` if despawned immediately or the call was ignored.

**Server-only**
- Has no effect when not running on the server.

---
