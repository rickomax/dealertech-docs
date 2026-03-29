---
layout: default
title: vector
parent: API Reference
nav_order: 25
---

# `vector`
{: .no_toc }

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

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `x` | `number` |  |
| `y` | `number` |  |
| `z` | `number` |  |

**Returns** `LuaVector`

---

### `random(  )`

{: .label .label-blue }
Static

**Returns** `LuaVector`

---

### `normalize( a )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |

**Returns** `LuaVector`

---

### `project( a, b )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |
| `b` | `LuaVector` |  |

**Returns** `LuaVector`

---

### `project_on_plane( a, b )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |
| `b` | `LuaVector` |  |

**Returns** `LuaVector`

---

### `lerp( a, b, t )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |
| `b` | `LuaVector` |  |
| `t` | `number` |  |

**Returns** `LuaVector`

---

### `lerp_angle( a, b, t )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `number` |  |
| `b` | `number` |  |
| `t` | `number` |  |

**Returns** `number`

---

### `dot( a, b )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |
| `b` | `LuaVector` |  |

**Returns** `number`

---

### `cross( a, b )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |
| `b` | `LuaVector` |  |

**Returns** `LuaVector`

---

### `length( a )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |

**Returns** `number`

---

### `squared_length( a )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `a` | `LuaVector` |  |

**Returns** `number`

---

### `make_angles( right, forward, up )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `right` | `LuaVector` |  |
| `forward` | `LuaVector` |  |
| `up` | `LuaVector` |  |

**Returns** `LuaVector`

---

### `make_vectors( luaAngles, right, forward, up )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `luaAngles` | `LuaVector` |  |
| `right` | `LuaVector` |  |
| `forward` | `LuaVector` |  |
| `up` | `LuaVector` |  |

---

## Properties

### `x`

**Type:** `number`

---

### `y`

**Type:** `number`

---

### `z`

**Type:** `number`

---

