---
layout: default
title: vector4
parent: API Reference
---

# `vector4`

A four-component vector object.

**C# type:** `LuaVector4`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaVector4.cs`

## Members

### `x`

Gets or sets the X component of the vector. Corresponds to the red channel when used as a colour.

`public float X`

### `y`

Gets or sets the Y component of the vector. Corresponds to the green channel when used as a colour.

`public float Y`

### `z`

Gets or sets the Z component of the vector. Corresponds to the blue channel when used as a colour.

`public float Z`

### `w`

Gets or sets the W component of the vector. Corresponds to the alpha channel when used as a colour.

`public float W`

### `create`

Creates a new vector4 with the given components. When used as a colour, pass RGBA values in the range [0, 1].

`public static LuaVector4 Create(float x, float y, float z, float w)`

### `normalize`

Returns the given vector scaled to a magnitude of 1.

`public static LuaVector4 Normalize(LuaVector4 a)`

### `project`

Projects vector <paramref name="a"/> onto vector <paramref name="b"/>.

`public static LuaVector4 Project(LuaVector4 a, LuaVector4 b)`

### `lerp`

Linearly interpolates between two vectors.

`public static LuaVector4 Lerp(LuaVector4 a, LuaVector4 b, float t)`

### `dot`

Returns the dot product of two vectors.

`public static float Dot(LuaVector4 a, LuaVector4 b)`

### `length`

Returns the magnitude (length) of the vector.

`public static float Length(LuaVector4 a)`

### `squared_length`

Returns the squared magnitude of the vector. Prefer this over `length` when comparing distances, as it avoids a square root.

`public static float SquaredLength(LuaVector4 a)`
