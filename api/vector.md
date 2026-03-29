---
layout: default
title: vector
parent: API Reference
nav_order: 25
---

# `vector`
{: .no_toc }

A three-component vector object.
{{: .fs-5 }}

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `create( x, y, z )`

{: .label .label-blue }
Static

Creates a new vector with the given components.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `x` | `number` | The X component. |
| `y` | `number` | The Y component. |
| `z` | `number` | The Z component. |

**Returns** `LuaVector` — A vector with the specified components.

---

### `random(  )`

{: .label .label-blue }
Static

Returns a random vector with a magnitude of 1 or less, uniformly distributed inside a unit sphere.

**Returns** `LuaVector` — A random vector inside the unit sphere.

---

### `normalize( a )`

{: .label .label-blue }
Static

Returns the given vector scaled to a magnitude of 1.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The vector to normalize. |

**Returns** `LuaVector` — The normalized vector.

---

### `project( a, b )`

{: .label .label-blue }
Static

Projects vector  onto vector .

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The vector to project. |
| `b` | `LuaVector` | The vector to project onto. |

**Returns** `LuaVector` — The projection of  onto .

---

### `project_on_plane( a, b )`

{: .label .label-blue }
Static

Projects vector  onto a plane defined by its normal vector .

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The vector to project. |
| `b` | `LuaVector` | The plane normal vector. |

**Returns** `LuaVector` — The component of  that lies on the plane.

---

### `lerp( a, b, t )`

{: .label .label-blue }
Static

Linearly interpolates between two vectors.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The start vector, returned when  is 0. |
| `b` | `LuaVector` | The end vector, returned when  is 1. |
| `t` | `number` | The interpolation factor, clamped to the range [0, 1]. |

**Returns** `LuaVector` — The interpolated vector.

---

### `lerp_angle( a, b, t )`

{: .label .label-blue }
Static

Linearly interpolates between two angles, correctly wrapping around 360 degrees.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `number` | The start angle in degrees, returned when  is 0. |
| `b` | `number` | The end angle in degrees, returned when  is 1. |
| `t` | `number` | The interpolation factor, clamped to the range [0, 1]. |

**Returns** `number` — The interpolated angle in degrees.

---

### `dot( a, b )`

{: .label .label-blue }
Static

Returns the dot product of two vectors.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The first vector. |
| `b` | `LuaVector` | The second vector. |

**Returns** `number` — The dot product. Returns 1 if the vectors point in the same direction, 0 if they are perpendicular, and -1 if they point in opposite directions (assuming both are normalized).

---

### `cross( a, b )`

{: .label .label-blue }
Static

Returns the cross product of two vectors.

The result is a vector perpendicular to both  and .

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The first vector. |
| `b` | `LuaVector` | The second vector. |

**Returns** `LuaVector` — The cross product vector.

---

### `length( a )`

{: .label .label-blue }
Static

Returns the magnitude (length) of the vector.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The vector to measure. |

**Returns** `number` — The magnitude of the vector.

**See also:** [`SquaredLength`](#squaredlength)

---

### `squared_length( a )`

{: .label .label-blue }
Static

Returns the squared magnitude of the vector.

Prefer this over  when comparing distances, as it avoids a square root.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` | The vector to measure. |

**Returns** `number` — The squared magnitude of the vector.

**See also:** [`Length`](#length)

---

### `make_angles( right, forward, up )`

{: .label .label-blue }
Static

Computes pitch/yaw/roll angles from a set of basis vectors.

The resulting angles represent the orientation described by "forward" and "up".

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `right` | `LuaVector` | The right basis vector. |
| `forward` | `LuaVector` | The forward basis vector. |
| `up` | `LuaVector` | The up basis vector. |

**Returns** `LuaVector` — The corresponding angles as a Lua vector.

---

### `make_vectors( luaAngles, right, forward, up )`

{: .label .label-blue }
Static

Decomposes angles into right, forward and up basis vectors.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `luaAngles` | `LuaVector` | The angles to decompose, as a Lua vector. |
| `right` | `LuaVector` | Set to the right basis vector. |
| `forward` | `LuaVector` | Set to the forward basis vector. |
| `up` | `LuaVector` | Set to the up basis vector. |

---

## Properties

### `x`

**Type:** `number`

Gets or sets the X component of the vector.

---

### `y`

**Type:** `number`

Gets or sets the Y component of the vector.

---

### `z`

**Type:** `number`

Gets or sets the Z component of the vector.

---

