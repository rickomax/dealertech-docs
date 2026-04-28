---
layout: default
title: math
parent: API Reference
---
# `math`

`math` provides common mathematical constants and functions.

All functions are static and accessed directly from the `math` table.

---

## Constants

### `math.pi() -> number`
Returns the value of π (pi).

---

### `math.deg2rad : number`
Conversion factor from degrees to radians.

---

### `math.rad2deg : number`
Conversion factor from radians to degrees.

---

## Random

### `math.random() -> number`
Returns a random value in the range `[0, 1]`.

---

### `math.random_range(min, max) -> number`
Returns a random value between `min` and `max`.

**Parameters**
- `min` (`number`)
- `max` (`number`)

---

## Trigonometry

All trigonometric functions take and return values in radians (use `math.deg2rad` / `math.rad2deg` to convert).

### `math.sin(v) -> number`
Returns the sine of `v` (in radians).

### `math.cos(v) -> number`
Returns the cosine of `v` (in radians).

### `math.tan(v) -> number`
Returns the tangent of `v` (in radians).

### `math.asin(v) -> number`
Returns the arcsine of `v`, in radians.

### `math.acos(v) -> number`
Returns the arccosine of `v`, in radians.

### `math.atan(v) -> number`
Returns the arctangent of `v`, in radians.

### `math.atan2(y, x) -> number`
Returns the angle in radians whose tangent is `y / x`.

---

## Basic Math

### `math.abs(v) -> number`
Returns the absolute value.

### `math.sign(v) -> number`
Returns the sign of the value (-1, 0, or 1).

### `math.sqrt(v) -> number`
Returns the square root.

### `math.pow(a, b) -> number`
Returns `a` raised to the power of `b`.

### `math.exp(v) -> number`
Returns e raised to the power of `v`.

### `math.log(v) -> number`
Natural logarithm.

### `math.log10(v) -> number`
Base-10 logarithm.

---

## Rounding

### `math.floor(v) -> number`
Rounds down.

### `math.ceil(v) -> number`
Rounds up.

### `math.round(v) -> number`
Rounds to the nearest integer.

---

## Min / Max / Clamp

### `math.min(a, b) -> number`
Returns the smaller value.

### `math.max(a, b) -> number`
Returns the larger value.

### `math.clamp(v, min, max) -> number`
Clamps `v` between `min` and `max`.

---

## Interpolation

### `math.lerp(a, b, t) -> number`
Linearly interpolates between `a` and `b`.

### `math.lerp_unclamped(a, b, t) -> number`
Linear interpolation without clamping `t`.

### `math.inverse_lerp(a, b, v) -> number`
Returns the interpolation factor `t` such that `lerp(a, b, t) = v`.

---

## Repetition

### `math.repeat(t, length) -> number`
Loops `t` so it wraps around `length`.

### `math.pingpong(t, length) -> number`
Returns a value that moves back and forth between `0` and `length`.
