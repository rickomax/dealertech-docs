---
title: input
parent: API Reference
---

# `input`

Provides access to the inputsystem.

**C# type:** `LuaInput`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaInput.cs`

## Members

### `bind`

Binds a Lua code string to an input action path. The code is evaluated every time the action is performed.

`public static void Bind(string path, string code)`

### `read_vector`

Reads a 2D axis value from a named input action and returns it as a Lua vector.

`public static LuaVector ReadVector(string path)`

### `read_input_down`

Returns whether a named input action was pressed during the current frame.

`public static float ReadInputDown(string path)`

### `read_input_pressed`

Returns whether a named input action is currently held down. Unlike <see cref="ReadInputDown"/>, this returns <c>1</c> for every frame the action remains pressed, not just the frame it was first pressed.

`public static float ReadInputPressed(string path)`

### `read_raw_float`

Reads the current float value directly from a raw device control path. Use this for low-level hardware access when named actions are not available or not appropriate (e.g. <c>&lt;Gamepad&gt;/leftStick/x</c>).

`public static float ReadRawFloat(string path)`

### `was_pressed`

Lua member <c>was_pressed</c>.

`public static float WasPressed(string path)`

### `is_held`

Returns whether a raw control is currently being held down.

`public static float IsHeld(string path)`
