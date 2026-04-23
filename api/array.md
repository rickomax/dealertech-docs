---
layout: default
title: array
parent: API Reference
---

# `array`

A dynamic, 1-indexed array of Lua values backed by a managed list. Unlike a plain Lua table, the array is reusable and can be preallocated through `array.create(capacity)`.

**C# type:** `LuaArray`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaArray.cs`

## Members

### `create`

Creates a new empty array with the given initial capacity.

`public static LuaArray Create(int capacity = 1)`

### `add`

Appends <paramref name="value"/> to the end of the array.

`public void Add(LuaValue value)`

### `get`

Returns the value stored at the given 1-based index.

`public LuaValue Get(int index)`

### `remove_at`

Removes the element at the given 1-based index, shifting subsequent elements left.

`public void RemoveAt(int index)`

### `clear`

Removes all elements from the array.

`public void Clear()`
