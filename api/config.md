---
layout: default
title: config
parent: API Reference
---

# `config`

Provides Lua access to the persistent configuration store (typically user preferences and console variables).

**C# type:** `LuaConfig`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaConfig.cs`

## Members

### `load`

Loads the configuration from disk, replacing any in-memory values.

`public static void Load()`

### `save`

Writes the current in-memory configuration to disk.

`public static void Save()`

### `get_number`

Returns the numeric value stored under the given key.

`public static float GetNumber(string key)`

### `set_number`

Sets the numeric value stored under the given key.

`public static void SetNumber(string key, float value)`

### `get_string`

Returns the string value stored under the given key.

`public static string GetString(string key)`

### `set_string`

Sets the string value stored under the given key.

`public static void SetString(string key, string value)`
