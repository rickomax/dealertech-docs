---
layout: default
title: vector
parent: API Reference
---

# `vector`

`vector` represents a 3D vector with `x`, `y`, and `z` components.

It provides common vector math operations and angle/vector conversion utilities.

---

## Properties

### `x` : `number`
Gets or sets the X component.

### `y` : `number`
Gets or sets the Y component.

### `z` : `number`
Gets or sets the Z component.

---

## Creation

### `vector.create(x, y, z) -> vector`
Creates a new vector with the given components.

**Parameters**
- `x` (`number`)
- `y` (`number`)
- `z` (`number`)

**Returns**
- `vector`

You can also call the namespace directly:

```lua
local v = vector(1, 2, 3)
```

---

### `vector.copy(a) -> vector`
Returns a new vector that is a copy of `a`.

**Parameters**
- `a` (`vector`)

---

### `vector:copy_from(other)`
Copies the components of `other` into this vector in place.

**Parameters**
- `other` (`vector`)

---

### `vector.random() -> vector`
Returns a random vector with magnitude `1` or less, uniformly distributed inside the unit sphere.

---

## Vector Operations

### `vector.normalize(a) -> vector`
Returns `a` scaled to a magnitude of `1`.

**Parameters**
- `a` (`vector`)

---

### `vector.project(a, b) -> vector`
Projects vector `a` onto vector `b`.

**Parameters**
- `a` (`vector`)
- `b` (`vector`)

---

### `vector.project_on_plane(a, b) -> vector`
Projects vector `a` onto a plane defined by its normal `b`.

**Parameters**
- `a` (`vector`)
- `b` (`vector`) — Plane normal.

---

### `vector.lerp(a, b, t) -> vector`
Linearly interpolates between `a` and `b`.

**Parameters**
- `a` (`vector`)
- `b` (`vector`)
- `t` (`number`) — Interpolation factor, clamped to `[0, 1]`.

---

### `vector.lerp_angle(a, b, t) -> number`
Linearly interpolates between two angles, correctly wrapping around 360 degrees.

**Parameters**
- `a` (`number`) — Start angle in degrees.
- `b` (`number`) — End angle in degrees.
- `t` (`number`) — Interpolation factor, clamped to `[0, 1]`.

---

### `vector.dot(a, b) -> number`
Returns the dot product of `a` and `b`.

Returns `1` if the vectors point the same way, `0` if perpendicular, `-1` if opposite (assuming both are normalized).

**Parameters**
- `a` (`vector`)
- `b` (`vector`)

---

### `vector.cross(a, b) -> vector`
Returns the cross product of `a` and `b`. The result is perpendicular to both inputs.

**Parameters**
- `a` (`vector`)
- `b` (`vector`)

---

### `vector.length(a) -> number`
Returns the magnitude (length) of `a`.

**Parameters**
- `a` (`vector`)

---

### `vector.squared_length(a) -> number`
Returns the squared magnitude of `a`. Prefer this over `length` when comparing distances, as it avoids a square root.

**Parameters**
- `a` (`vector`)

---

## Angle / Direction Utilities

### `vector.make_angles(right, forward, up) -> vector`
Builds Euler angles (pitch / yaw / roll) from three basis vectors.

**Parameters**
- `right` (`vector`)
- `forward` (`vector`)
- `up` (`vector`)

**Returns**
- `vector` — The orientation as pitch / yaw / roll.

---

### `vector.make_vectors(angles, right, forward, up)`
Decomposes an angles vector into right, forward and up basis vectors.

**Parameters**
- `angles` (`vector`)
- `right` (`vector`, out)
- `forward` (`vector`, out)
- `up` (`vector`, out)

The output vectors are passed by reference and overwritten with the resulting basis vectors.

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
local origin  = vector.create(0, 0, 64)
local forward = vector.create(0, 0, 0)
local right   = vector.create(0, 0, 0)
local up      = vector.create(0, 0, 0)
vector.make_vectors(self:get_angles(), right, forward, up)

local target = origin + forward * 256
local mid    = vector.lerp(origin, target, 0.5)

local dist_sq = vector.squared_length(target - origin)
```
