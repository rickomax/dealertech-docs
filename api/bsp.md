---
title: bsp
parent: API Reference
---

# `bsp`

Provides Lua access to the loaded BSP (Binary Space Partitioning) map, including map discovery and content queries.

**C# type:** `LuaBSP`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaBSP.cs`

## Members

### `get_maps`

Returns the list of available BSP maps (without the `.bsp` extension) found under the `maps` directory.

`public static LuaTable GetMaps()`

### `point_contents`

Returns the contents flags of the BSP leaf that contains the given point.

`public static int PointContents(LuaVector vector)`

### `trace_contents`

Traces a line through the BSP tree and fills <paramref name="result"/> with any contents hit.

`public static void TraceContents(LuaVector start, LuaVector end, LuaTraceResult result)`
