---
layout: default
title: movement
parent: API Reference
---

# `movement`

Output movement written by the Lua `process_movement` function each tick. The engine reads these values back to apply the new state to the player.

**C# type:** `LuaMovement`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaMovementData.cs`

## Members

### `angles`

The new pitch/yaw/roll angles to apply to the player.

`public LuaVector Angles`

### `velocity`

The new velocity vector to apply to the player.

`public LuaVector Velocity`

### `is_grounded`

Whether the player should be considered grounded after this tick.

`public bool IsGrounded`

### `flag1`

Generic script-defined flag written back to the server tick state.

`public bool Flag1`

### `flag2`

Generic script-defined flag written back to the server tick state.

`public bool Flag2`

### `flag3`

Generic script-defined flag written back to the server tick state.

`public bool Flag3`

### `flag4`

Generic script-defined flag written back to the server tick state.

`public bool Flag4`
