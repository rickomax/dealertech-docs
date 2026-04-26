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

### `math.sin(v) -> number`
### `math.cos(v) -> number`
### `math.tan(v) -> number`
### `math.asin(v) -> number`
### `math.acos(v) -> number`
### `math.atan(v) -> number`
### `math.atan2(y, x) -> number`

Standard trigonometric functions.

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

---

## Example

```lua
local angle = 45 * math.deg2rad
local s = math.sin(angle)

local r = math.random_range(10, 20)

local clamped = math.clamp(15, 0, 10)
```
