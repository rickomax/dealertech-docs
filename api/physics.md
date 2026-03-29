---
layout: default
title: physics
parent: API Reference
nav_order: 17
---

# `physics`
{: .no_toc }

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `get_entities_in_bounds( mins, maxs, count )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `mins` | `LuaVector` |  |
| `maxs` | `LuaVector` |  |
| `count` | `number` |  |

**Returns** `LuaArray`

---

### `trace_hull( luaStart, luaEnd, luaMin, luaMax, collisionType, ignore, getTraceContents, debug )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `luaStart` | `LuaVector` |  |
| `luaEnd` | `LuaVector` |  |
| `luaMin` | `LuaVector` |  |
| `luaMax` | `LuaVector` |  |
| `collisionType` | `number` |  |
| `ignore` | `GameEntity` |  |
| `getTraceContents` | `boolean` |  |
| `debug` | `boolean` |  |

**Returns** `LuaTraceResult`

---

### `trace_line( luaStart, luaEnd, collisionType, ignore, getTraceContents, debug )`

{: .label .label-blue }
Static

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `luaStart` | `LuaVector` |  |
| `luaEnd` | `LuaVector` |  |
| `collisionType` | `number` |  |
| `ignore` | `GameEntity` |  |
| `getTraceContents` | `boolean` |  |
| `debug` | `boolean` |  |

**Returns** `LuaTraceResult`

---

