---
layout: default
title: entity_state
parent: API Reference
---
# `entity_state`

`entity_state` represents a single state entry used by the engine's entity state machine.

Each state defines:
- The animation frame to use.
- The duration of the state.
- Optional Lua code to execute when the state runs.

---

## Fields

### `frame` : `string|number`
Animation frame applied when the state begins.

Accepts either:
- a `string` — the frame name as defined in the entity's model, or
- a `number` — a 1-based frame index.

---

### `interval` : `number`
Duration (in seconds) that the entity remains in this state before advancing.

---

### `code` : `function|any`
Lua function or value executed when the state is processed.

Typically this is a function containing the logic to run during this state.

---

## Creation

### `entity_state.create(frame, interval, code) -> integer`

Creates a new entity state and returns its state index. The returned index is used with `entity:set_state`.

**Parameters**
- `frame` (`string|number`) — Animation frame name, or a 1-based frame index.
- `interval` (`number`) — Duration in seconds.
- `code` (`function|any`) — Lua function or value to execute for this state.

**Returns**
- `integer` — The state index.
