---
title: entity_state
parent: API Reference
---

# `entity_state`

Represents a single named animation/logic state that an entity can switch to. Created from Lua via `entity_state.create` and registered in the global state table.

**C# type:** `LuaEntityState`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaEntityState.cs`

## Members

### `frame`

The animation frame name played while this state is active.

`public string Frame`

### `interval`

The tick interval, in seconds, at which the state's code runs.

`public float Interval`

### `code`

The Lua value (string or function) executed at each state tick. When a function is supplied, it may return the name of the next state to enter.

`public LuaValue Code`

### `create`

Registers a new state with the given frame, tick interval, and code, and returns its index.

`public static int Create(string frame, float interval, LuaValue code)`
