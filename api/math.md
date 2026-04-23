---
layout: default
title: math
parent: API Reference
---

# `math`

Exposes common numeric helpers, trigonometry, and random-number utilities to Lua.

**C# type:** `LuaMath`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaMath.cs`

## Members

### `pi`

Returns the value of Pi (3.14159...).

`public static float Pi()`

### `deg2rad`

Conversion factor from degrees to radians.

`public static float Deg2Rad`

### `rad2deg`

Conversion factor from radians to degrees.

`public static float Rad2Deg`

### `random`

Returns a deterministic random number in the range [0, 1]. The underlying generator is seeded from the current server tick so that all peers agree on the result.

`public static float Random()`

### `random_range`

Returns a deterministic random number in the range [<paramref name="min"/>, <paramref name="max"/>]. The underlying generator is seeded from the current server tick so that all peers agree on the result.

`public static float RandomRange(float min, float max)`

### `sin`

Returns the sine of the given angle in radians.

`public static float Sin(float v)`

### `cos`

Returns the cosine of the given angle in radians.

`public static float Cos(float v)`

### `tan`

Returns the tangent of the given angle in radians.

`public static float Tan(float v)`

### `asin`

Returns the arc sine of <paramref name="v"/> in radians.

`public static float Asin(float v)`

### `acos`

Returns the arc cosine of <paramref name="v"/> in radians.

`public static float Acos(float v)`

### `atan`

Returns the arc tangent of <paramref name="v"/> in radians.

`public static float Atan(float v)`

### `atan2`

Returns the angle in radians whose tangent is <paramref name="y"/>/<paramref name="x"/>, using the signs of both arguments to determine the correct quadrant.

`public static float Atan2(float y, float x)`

### `abs`

Returns the absolute value of <paramref name="v"/>.

`public static float Abs(float v)`

### `sign`

Returns the sign of <paramref name="v"/>.

`public static float Sign(float v)`

### `sqrt`

Returns the square root of <paramref name="v"/>.

`public static float Sqrt(float v)`

### `pow`

Returns <paramref name="a"/> raised to the power of <paramref name="b"/>.

`public static float Pow(float a, float b)`

### `exp`

Returns e raised to the power of <paramref name="v"/>.

`public static float Exp(float v)`

### `log`

Returns the natural (base-e) logarithm of <paramref name="v"/>.

`public static float Log(float v)`

### `log10`

Returns the base-10 logarithm of <paramref name="v"/>.

`public static float Log10(float v)`

### `floor`

Returns the largest integer less than or equal to <paramref name="v"/>.

`public static float Floor(float v)`

### `ceil`

Returns the smallest integer greater than or equal to <paramref name="v"/>.

`public static float Ceil(float v)`

### `round`

Returns <paramref name="v"/> rounded to the nearest integer.

`public static float Round(float v)`

### `min`

Returns the smallest of two values.

`public static float Min(float a, float b)`

### `max`

Returns the largest of two values.

`public static float Max(float a, float b)`

### `clamp`

Clamps <paramref name="v"/> into the range [<paramref name="min"/>, <paramref name="max"/>].

`public static float Clamp(float v, float min, float max)`

### `lerp`

Linearly interpolates between <paramref name="a"/> and <paramref name="b"/>. The interpolation factor is clamped to [0, 1].

`public static float Lerp(float a, float b, float t)`

### `lerp_unclamped`

Linearly interpolates between <paramref name="a"/> and <paramref name="b"/> without clamping the interpolation factor.

`public static float LerpUnclamped(float a, float b, float t)`

### `inverse_lerp`

Returns the interpolation factor `t` in the range [0, 1] such that `lerp(a, b, t) == v`.

`public static float InverseLerp(float a, float b, float v)`

### `repeat`

Wraps <paramref name="t"/> into the range [0, <paramref name="length"/>] so that it never exceeds <paramref name="length"/> or goes negative.

`public static float Repeat(float t, float length)`

### `pingpong`

Returns a value that oscillates back and forth between 0 and <paramref name="length"/> as <paramref name="t"/> increases.

`public static float PingPong(float t, float length)`
