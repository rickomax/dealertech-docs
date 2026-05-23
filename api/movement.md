---
layout: default
title: movement
parent: API Reference
---

# `movement`

`movement` is the output movement state written by the Lua `process_movement` function each tick. The engine reads these fields after the callback returns to build the next movement packet.

Passed to `player.process_movement(self, input_data, in_move, out_move)` as `out_move`.

> Note: `movement` does not have a `position` field — the engine derives it from the resulting collision step.

---

## Fields

### `angles` : `vector`
The new pitch/yaw/roll angles to apply to the player.

### `velocity` : `vector`
The new velocity vector to apply to the player.

### `is_grounded` : `boolean`
Whether the player should be considered grounded after this tick.

### `flag1` : `boolean`
Generic script-defined flag written back to the server tick state.

### `flag2` : `boolean`
Generic script-defined flag written back to the server tick state.

### `flag3` : `boolean`
Generic script-defined flag written back to the server tick state.

### `flag4` : `boolean`
Generic script-defined flag written back to the server tick state.
