---
title: math
parent: API Reference
---

# `math`

Lua API object exposed as <c>math</c>.

**C# type:** `LuaMath`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaMath.cs`

## Members

### `pi`

Lua member <c>pi</c>.

`public static float Pi()`

### `deg2rad`

Lua member <c>deg2rad</c>.

`public static float Deg2Rad => Mathf.Deg2Rad;`

### `rad2deg`

Lua member <c>rad2deg</c>.

`public static float Rad2Deg => Mathf.Rad2Deg;`

### `random`

Lua member <c>random</c>.

`public static float Random()`

### `random_range`

Lua member <c>random_range</c>.

`public static float RandomRange(float min, float max)`

### `sin`

Lua member <c>sin</c>.

`public static float Sin(float v) => Mathf.Sin(v);`

### `cos`

Lua member <c>cos</c>.

`public static float Cos(float v) => Mathf.Cos(v);`

### `tan`

Lua member <c>tan</c>.

`public static float Tan(float v) => Mathf.Tan(v);`

### `asin`

Lua member <c>asin</c>.

`public static float Asin(float v) => Mathf.Asin(v);`

### `acos`

Lua member <c>acos</c>.

`public static float Acos(float v) => Mathf.Acos(v);`

### `atan`

Lua member <c>atan</c>.

`public static float Atan(float v) => Mathf.Atan(v);`

### `atan2`

Lua member <c>atan2</c>.

`public static float Atan2(float y, float x) => Mathf.Atan2(y, x);`

### `abs`

Lua member <c>abs</c>.

`public static float Abs(float v) => Mathf.Abs(v);`

### `sign`

Lua member <c>sign</c>.

`public static float Sign(float v) => Mathf.Sign(v);`

### `sqrt`

Lua member <c>sqrt</c>.

`public static float Sqrt(float v) => Mathf.Sqrt(v);`

### `pow`

Lua member <c>pow</c>.

`public static float Pow(float a, float b) => Mathf.Pow(a, b);`

### `exp`

Lua member <c>exp</c>.

`public static float Exp(float v) => Mathf.Exp(v);`

### `log`

Lua member <c>log</c>.

`public static float Log(float v) => Mathf.Log(v);`

### `log10`

Lua member <c>log10</c>.

`public static float Log10(float v) => Mathf.Log10(v);`

### `floor`

Lua member <c>floor</c>.

`public static float Floor(float v) => Mathf.Floor(v);`

### `ceil`

Lua member <c>ceil</c>.

`public static float Ceil(float v) => Mathf.Ceil(v);`

### `round`

Lua member <c>round</c>.

`public static float Round(float v) => Mathf.Round(v);`

### `min`

Lua member <c>min</c>.

`public static float Min(float a, float b) => Mathf.Min(a, b);`

### `max`

Lua member <c>max</c>.

`public static float Max(float a, float b) => Mathf.Max(a, b);`

### `clamp`

Lua member <c>clamp</c>.

`public static float Clamp(float v, float min, float max)`

### `lerp`

Lua member <c>lerp</c>.

`public static float Lerp(float a, float b, float t)`

### `lerp_unclamped`

Lua member <c>lerp_unclamped</c>.

`public static float LerpUnclamped(float a, float b, float t)`

### `inverse_lerp`

Lua member <c>inverse_lerp</c>.

`public static float InverseLerp(float a, float b, float v)`

### `repeat`

Lua member <c>repeat</c>.

`public static float Repeat(float t, float length)`

### `pingpong`

Lua member <c>pingpong</c>.

`public static float PingPong(float t, float length)`
