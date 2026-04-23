---
title: vector
parent: API Reference
---

# `vector`

A three-component vector object.

**C# type:** `LuaVector`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaVector.cs`

## Members

### `x`

Gets or sets the X component of the vector.

`public float X`

### `y`

Gets or sets the Y component of the vector.

`public float Y`

### `z`

Gets or sets the Z component of the vector.

`public float Z`

### `create`

Creates a new vector with the given components.

`public static LuaVector Create(float x, float y, float z)`

### `copy`

Returns a new vector with the same components as <paramref name="instance"/>.

`public static LuaVector Copy(LuaVector instance)`

### `copy_from`

Copies the components of <paramref name="instance"/> into this vector in place.

`public void CopyFrom(LuaVector instance)`

### `random`

Returns a random vector with a magnitude of 1 or less, uniformly distributed inside a unit sphere.

`public static LuaVector Random()`

### `normalize`

Returns the given vector scaled to a magnitude of 1.

`public static LuaVector Normalize(LuaVector a)`

### `project`

Projects vector <paramref name="a"/> onto vector <paramref name="b"/>.

`public static LuaVector Project(LuaVector a, LuaVector b)`

### `project_on_plane`

Projects vector <paramref name="a"/> onto a plane defined by its normal vector <paramref name="b"/>.

`public static LuaVector ProjectOnPlane(LuaVector a, LuaVector b)`

### `lerp`

Linearly interpolates between two vectors.

`public static LuaVector Lerp(LuaVector a, LuaVector b, float t)`

### `lerp_angle`

Linearly interpolates between two angles, correctly wrapping around 360 degrees.

`public static float LerpAngle(float a, float b, float t)`

### `dot`

Returns the dot product of two vectors.

`public static float Dot(LuaVector a, LuaVector b)`

### `cross`

Returns the cross product of two vectors. The result is a vector perpendicular to both <paramref name="a"/> and <paramref name="b"/>.

`public static LuaVector Cross(LuaVector a, LuaVector b)`

### `length`

Returns the magnitude (length) of the vector.

`public static float Length(LuaVector a)`

### `squared_length`

Returns the squared magnitude of the vector. Prefer this over `length` when comparing distances, as it avoids a square root.

`public static float SquaredLength(LuaVector a)`

### `make_angles`

Computes pitch/yaw/roll angles from a set of basis vectors. The resulting angles represent the orientation described by "forward" and "up".

`public static LuaVector MakeAngles(LuaVector right, LuaVector forward, LuaVector up)`

### `make_vectors`

Decomposes angles into right, forward and up basis vectors.

`public static void MakeVectors(LuaVector luaAngles, ref LuaVector right, ref LuaVector forward, ref LuaVector up)`
