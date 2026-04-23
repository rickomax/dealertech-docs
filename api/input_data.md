---
layout: default
title: input_data
parent: API Reference
---

# `input_data`

A fixed-size float buffer used by the input system to pass raw input values. Each slot corresponds to one input axis or button value, stored as a float. There are 32 available slots. An instance of this object is passed to the Lua `read_input` and `process_actions` functions each frame.

**C# type:** `LuaInputData`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaInputData.cs`

## Members

### `indexer`

Gets or sets the raw float input value at the given index.

`public float this[int index]`
