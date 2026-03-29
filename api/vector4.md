---
layout: default
title: vector4
parent: API Reference
nav_order: 26
---

# `vector4`
{: .no_toc }

A four-component vector object.
{{: .fs-5 }}

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `create( x, y, z, w )`

{: .label .label-blue }
Static

Creates a new vector4 with the given components.

When used as a colour, pass RGBA values in the range [0, 1].

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `x` | `number` | The X component (red channel). |
| `y` | `number` | The Y component (green channel). |
| `z` | `number` | The Z component (blue channel). |
| `w` | `number` | The W component (alpha channel). |

**Returns** `LuaVector4` — A vector4 with the specified components.

---

### `normalize( a )`

{: .label .label-blue }
Static

Returns the given vector scaled to a magnitude of 1.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector4` | The vector to normalize. |

**Returns** `LuaVector4` — The normalized vector.

---

### `project( a, b )`

{: .label .label-blue }
Static

Projects vector  onto vector .

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector4` | The vector to project. |
| `b` | `LuaVector4` | The vector to project onto. |

**Returns** `LuaVector4` — The projection of  onto .

---

### `lerp( a, b, t )`

{: .label .label-blue }
Static

Linearly interpolates between two vectors.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector4` | The start vector, returned when  is 0. |
| `b` | `LuaVector4` | The end vector, returned when  is 1. |
| `t` | `number` | The interpolation factor, clamped to the range [0, 1]. |

**Returns** `LuaVector4` — The interpolated vector.

---

### `dot( a, b )`

{: .label .label-blue }
Static

Returns the dot product of two vectors.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector4` | The first vector. |
| `b` | `LuaVector4` | The second vector. |

**Returns** `number` — The dot product of  and .

---

### `length( a )`

{: .label .label-blue }
Static

Returns the magnitude (length) of the vector.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector4` | The vector to measure. |

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
| `a` | `LuaVector4` | The vector to measure. |

**Returns** `number` — The squared magnitude of the vector.

**See also:** [`Length`](#length)

---

## Properties

### `x`

**Type:** `number`

Gets or sets the X component of the vector.

Corresponds to the red channel when used as a colour.

---

### `y`

**Type:** `number`

Gets or sets the Y component of the vector.

Corresponds to the green channel when used as a colour.

---

### `z`

**Type:** `number`

Gets or sets the Z component of the vector.

Corresponds to the blue channel when used as a colour.

---

### `w`

**Type:** `number`

Gets or sets the W component of the vector.

Corresponds to the alpha channel when used as a colour.

---

