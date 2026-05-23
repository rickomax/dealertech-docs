---
layout: default
title: "`entity:set_state(stateIndex)`"
parent: entity
grand_parent: API Reference
nav_order: 50
---

# `entity:set_state(stateIndex)`

Assigns the current state index for this entity.

**Parameters**
- `stateIndex` (`integer`) — A state index returned by `entity_state.create`. Pass `-1` to clear the current state.

**Behavior**
- If the new state has a non-empty `frame`, the entity frame is updated immediately.
- If the new state's `interval` is negative, it will not automatically advance.
- Otherwise the state is scheduled to advance after `interval` seconds.

---

## Networked Variables
