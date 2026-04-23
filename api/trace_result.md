---
title: trace_result
parent: API Reference
---

# `trace_result`

Represents the result of a physics trace query such as `physics.trace_line` or `physics.trace_hull`.

**C# type:** `LuaTraceResult`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaTraceResult.cs`

## Members

### `start_solid`

`true` if the trace started inside a solid volume.

`public bool StartSolid`

### `fraction`

The fraction of the trace's length, in the range [0, 1], at which the hit occurred. A value of `1` indicates the trace completed without hitting anything.

`public float Fraction`

### `end_position`

The final position of the trace; equal to the hit point on collision, or the trace's end point otherwise.

`public LuaVector EndPosition`

### `normal`

The surface normal at the hit point, or a zero vector when nothing was hit.

`public LuaVector Normal`

### `distance`

The distance along the trace at which the hit occurred.

`public float Distance`

### `hit_table`

The Lua instance table of the hit entity, or `nil` when nothing was hit.

`public LuaTable HitTable`
