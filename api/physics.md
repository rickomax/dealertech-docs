---
layout: default
title: physics
parent: API Reference
---

# `physics`

Provides Lua-exposed physics queries and trace operations.

**C# type:** `LuaPhysics`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaPhysics.cs`

## Members

### `get_entities_in_bounds`

Returns entities inside an axis-aligned bounds volume.

`public static LuaArray GetEntitiesInBounds(LuaVector mins, LuaVector maxs, out int count)`

### `trace_hull`

Traces a swept box from start to end and returns collision details.

`public static LuaTraceResult TraceHull(LuaVector luaStart, LuaVector luaEnd, LuaVector luaMin, LuaVector luaMax, int collisionType, GameEntity ignore, bool debug)`

### `trace_line`

Traces a line from start to end and returns first collision details.

`public static LuaTraceResult TraceLine(LuaVector luaStart, LuaVector luaEnd, int collisionType, GameEntity ignore, bool debug)`
