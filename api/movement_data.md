---
title: movement_data
parent: API Reference
---

# `movement_data`

Input movement snapshot passed into the Lua `process_movement` function each tick, describing the player's state before movement is applied.

**C# type:** `LuaMovementData`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaMovementData.cs`

## Members

### `angles`

The current pitch/yaw/roll angles of the player.

`public LuaVector Angles`

### `position`

The current world-space position of the player.

`public LuaVector Position`

### `velocity`

The current velocity of the player.

`public LuaVector Velocity`

### `is_grounded`

Whether the player was grounded at the start of this tick.

`public bool IsGrounded`

### `was_grounded`

Whether the player was grounded at the end of the previous tick.

`public bool WasGrounded`

### `flag1`

Generic script-defined flag read from the previous tick state.

`public bool Flag1`

### `flag2`

Generic script-defined flag read from the previous tick state.

`public bool Flag2`

### `flag3`

Generic script-defined flag read from the previous tick state.

`public bool Flag3`

### `flag4`

Generic script-defined flag read from the previous tick state.

`public bool Flag4`
