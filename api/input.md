---
layout: default
title: input
parent: API Reference
nav_order: 10
---

# `input`
{: .no_toc }

Provides access to the inputsystem.
{{: .fs-5 }}

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `bind( path, code )`

{: .label .label-blue }
Static

Binds a Lua code string to an input action path.

The code is evaluated every time the action is performed.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `path` | `string` | The binding path to listen on (e.g. <Keyboard>/space). |
| `code` | `string` | The Lua code string to evaluate when the action fires. |

---

### `read_vector( path )`

{: .label .label-blue }
Static

Reads a 2D axis value from a named input action and returns it as a Lua vector.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `path` | `string` | The name of the input action to read (e.g. "Move"). |

**Returns** `LuaVector` — The action's current 2D value as a Lua vector with Z set to 0, or a zero vector if the action is not found.

---

### `read_input_down( path )`

{: .label .label-blue }
Static

Returns whether a named input action was pressed during the current frame.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `path` | `string` | The name of the input action to query (e.g. "Jump"). |

**Returns** `number` — 1 if the action was pressed this frame; 0 otherwise. Returns 0 if the action is not found.

**See also:** [`ReadInputPressed`](#readinputpressed)

---

### `read_input_pressed( path )`

{: .label .label-blue }
Static

Returns whether a named input action is currently held down.

Unlike , this returns 1 for every frame the action remains pressed, not just the frame it was first pressed.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `path` | `string` | The name of the input action to query (e.g. "Jump"). |

**Returns** `number` — 1 if the action is currently pressed; 0 otherwise. Returns 0 if the action is not found.

**See also:** [`ReadInputDown`](#readinputdown)

---

### `read_raw_float( path )`

{: .label .label-blue }
Static

Reads the current float value directly from a raw device control path.

Use this for low-level hardware access when named actions are not available or not appropriate (e.g. <Gamepad>/leftStick/x).

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `path` | `string` | The raw control path to read from. |

**Returns** `number` — The current float value of the control, or 0 if the control is not found or is not a float control.

---

