---
layout: default
title: player
parent: API Reference
nav_order: 3
---

# `player`
{: .no_toc }

Extends  with player-specific Lua bindings for input, movement, camera and view model control.
{{: .fs-5 }}

**Inherits:** `GameEntity`

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `is_owner(  )`

Returns whether this player entity is owned by the local client.

**Returns** `boolean` — true if the local client owns this player entity.

---

### `get_punch_angles(  )`

Returns the current punch angles applied to the player's view.

**Returns** `LuaVector` — The punch angles as a Lua vector.

---

### `get_view_height(  )`

Returns the current view height of the player.

**Returns** `number` — The view height value.

---

### `get_view_offset(  )`

Returns the view offset of the player relative to its origin.

**Returns** `LuaVector` — The view offset as a Lua vector, or the default value if not called on the server.

---

### `get_view_origin(  )`

Returns the world position of the player's camera.

**Returns** `LuaVector` — The camera world position as a Lua vector, or the default value if not called on the server.

---

### `set_punch_angles( value )`

Sets the punch angles applied to the player's view.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `LuaVector` | The new punch angles as a Lua vector. |

---

### `set_roll( value )`

Sets the roll angle of the player.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new roll angle in degrees. |

---

### `set_sway_amount( value )`

Sets the weapon sway amount for this player.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new sway amount. |

---

### `set_third_person( value )`

Enables or disables third-person camera mode for this player.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `boolean` | true to enable third-person mode; false for first-person. |

---

### `set_view_frame( name )`

Sets the current animation frame of the player's view model.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `name` | `string` | The animation frame name. |

---

### `set_view_height( height )`

Sets the view height of the player.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `height` | `number` | The new view height value. |

---

### `set_view_model( filename )`

Sets the view model displayed in first-person for this player.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `filename` | `string` | The MDL filename of the view model. |

---

### `set_view_offset( offset )`

Sets the view offset of the player relative to its origin.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `offset` | `LuaVector` | The new view offset as a Lua vector. |

---

### `set_weapon_offset( offset )`

Sets the weapon model position offset.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `offset` | `LuaVector` | The new weapon offset as a Lua vector. |

---

