---
layout: default
title: lights
parent: API Reference
---

# `lights`

Provides Lua access to the global light style table and helpers for spawning dynamic or static lights on the server.

**C# type:** `LuaLights`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaLights.cs`

## Members

### `get_computed_style`

Returns the currently computed intensity for the light style at the given index. Only runs on the server; returns `0` otherwise.

`public static float GetComputedStyle(int index)`

### `set_style`

Sets the pattern string for a light style. Each character represents the relative intensity at that tick (e.g. `"mmamammmmammamamaaamammma"`). Only runs on the server.

`public static void SetStyle(int index, string style)`

### `create_light`

Spawns a new networked light on the server and returns it.

`public static GameLight CreateLight(LuaVector position, LuaVector color, float intensity, float radius, bool isStatic, GameEntity parent = null)`
