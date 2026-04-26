---
layout: default
title: vector4
parent: API Reference
---

# `vector4`

`vector4` represents a 4D vector with `x`, `y`, `z`, and `w` components.

It is also commonly used as an RGBA colour, where each component is in the range `[0, 1]` and `w` represents the alpha channel.

It provides common vector math operations.

---

## Properties

### `x` : `number`
Gets or sets the X component (red channel when used as a colour).

### `y` : `number`
Gets or sets the Y component (green channel when used as a colour).

### `z` : `number`
Gets or sets the Z component (blue channel when used as a colour).

### `w` : `number`
Gets or sets the W component (alpha channel when used as a colour).

---

## Creation

### `vector4.create(x, y, z, w) -> vector4`
Creates a new 4D vector.

**Parameters**
- `x` (`number`) — X component (red channel).
- `y` (`number`) — Y component (green channel).
- `z` (`number`) — Z component (blue channel).
- `w` (`number`) — W component (alpha channel).

**Returns**
- `vector4`

You can also call the namespace directly:

```lua
local c = vector4(1, 0, 0, 1)
```

---

## Vector Operations

### `vector4.normalize(a) -> vector4`
Returns a normalized copy of `a` (magnitude `1`).

**Parameters**
- `a` (`vector4`)

---

### `vector4.project(a, b) -> vector4`
Projects vector `a` onto vector `b`.

**Parameters**
- `a` (`vector4`)
- `b` (`vector4`)

---

### `vector4.lerp(a, b, t) -> vector4`
Linearly interpolates between `a` and `b`.

**Parameters**
- `a` (`vector4`)
- `b` (`vector4`)
- `t` (`number`) — Interpolation factor, clamped to `[0, 1]`.

---

### `vector4.dot(a, b) -> number`
Returns the dot product of `a` and `b`.

**Parameters**
- `a` (`vector4`)
- `b` (`vector4`)

---

### `vector4.length(a) -> number`
Returns the magnitude of `a`.

**Parameters**
- `a` (`vector4`)

---

### `vector4.squared_length(a) -> number`
Returns the squared magnitude of `a`. Prefer this over `length` when comparing distances.

**Parameters**
- `a` (`vector4`)

---

## Operators

### Addition
`c = a + b`

### Subtraction
`c = a - b`

### Scalar Multiplication
`c = a * s`

### Scalar Division
`c = a / s`

### Equality
`a == b`

### String Conversion
`tostring(a)`

---

## Example

```lua
-- A semi-transparent red colour
local red = vector4.create(1, 0, 0, 0.5)

-- Linearly fade between two colours
local from = vector4.create(1, 1, 1, 1)
local to   = vector4.create(0, 0, 0, 1)
local mid  = vector4.lerp(from, to, 0.5)
```
