---
layout: default
title: "`entity_state.create(frame, interval, code) -> integer`"
parent: entity_state
grand_parent: API Reference
nav_order: 4
---

# `entity_state.create(frame, interval, code) -> integer`

Creates a new entity state and returns its state index. The returned index is used with `entity:set_state`.

**Parameters**
- `frame` (`string|number`) — Animation frame name, or a 1-based frame index.
- `interval` (`number`) — Duration in seconds.
- `code` (`function|any`) — Lua function or value to execute for this state.

**Returns**
- `integer` — The state index.
