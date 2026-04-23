---
layout: default
title: particles
parent: API Reference
---

# `particles`

Provides Lua access to the particle system. All calls are server-side.

**C# type:** `LuaParticles`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaParticles.cs`

## Members

### `spawn`

Spawns a burst of particles from the effect file at the given origin. Only runs on the server.

`public static void Spawn(string filename, LuaVector origin, float duration, int count)`
