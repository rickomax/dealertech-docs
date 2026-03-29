---
layout: default
title: lights
parent: API Reference
nav_order: 12
---

# `lights`
{: .no_toc }

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `get_computed_style( index )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `index` | `number` |  |

**Returns** `number`

---

### `set_style( index, style )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `index` | `number` |  |
| `style` | `string` |  |

---

### `create_light( position, color, intensity, radius, isStatic, parent )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `position` | `LuaVector` |  |
| `color` | `LuaVector` |  |
| `intensity` | `number` |  |
| `radius` | `number` |  |
| `isStatic` | `boolean` |  |
| `parent` | `GameEntity` |  *(default: `null`)* |

**Returns** `GameLight`

---

