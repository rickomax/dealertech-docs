---
layout: default
title: entity
parent: API Reference
nav_order: 1
---

# `entity`
{: .no_toc }

Represents entity properties, movement, state, and network variables to Lua scripts.
{{: .fs-5 }}

**Inherits:** `NetworkBehaviour`

---

## Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Methods

### `get_velocity(  )`

Returns the current velocity of the entity.

**Returns** `LuaVector` — The entity velocity as a Lua vector.

---

### `get_angle(  )`

Returns the current yaw angle of the entity.

**Returns** `number` — The entity yaw angle in degrees.

---

### `get_angles(  )`

Returns the current angles of the entity.

**Returns** `LuaVector` — The entity pitch, yaw and roll angles as a Lua vector.

---

### `get_brush_size(  )`

Returns the brush size of the entity.

**Returns** `LuaVector` — The brush extents as a Lua vector, or a zero vector if the entity solid type is not .

---

### `get_frame(  )`

Returns the current animation frame name of the entity.

**Returns** `string` — The current animation frame name.

---

### `get_health(  )`

Returns the current health of the entity.

**Returns** `number` — The entity health value.

---

### `get_model(  )`

Returns the current model filename of the entity.

**Returns** `string` — The MDL filename.

---

### `get_origin(  )`

Returns the current origin of the entity.

**Returns** `LuaVector` — The entity world position as a Lua vector.

---

### `get_size( mins, maxs )`

Returns the axis-aligned bounding box of the entity.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `mins` | `LuaVector` | The minimum bounds corner. |
| `maxs` | `LuaVector` | The maximum bounds corner. |

---

### `get_state(  )`

Returns the current state index of the entity.

**Returns** `string` — The current state index as a string.

---

### `is_grounded(  )`

Returns whether the entity is grounded.

**Returns** `boolean` — true if the entity is grounded.

---

### `set_angle( value )`

Sets the entity yaw angle.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new yaw angle in degrees. |

---

### `set_angles( angles )`

Sets the entity pitch, yaw and roll angles.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `angles` | `LuaVector` | The new angles as a Lua vector. |

---

### `set_frame( name )`

Sets the entity animation frame.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `name` | `string` | The animation frame name. |

---

### `set_health( value )`

Sets the entity health.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new health value. |

---

### `set_label( label )`

Sets the debug label text displayed on the entity.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `label` | `string` | The label text to display. |

---

### `set_model( filename )`

Sets the entity model.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `filename` | `string` | The MDL filename. |

---

### `set_move_type( value )`

Sets the entity move type.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new move type. |

---

### `set_origin( origin )`

Sets the entity origin.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `origin` | `LuaVector` | The new world position as a Lua vector. |

---

### `set_size( min, max )`

Sets the entity axis-aligned bounding box.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `min` | `LuaVector` | The minimum bounds corner. |
| `max` | `LuaVector` | The maximum bounds corner. |

---

### `set_solid( value )`

Sets the entity solid type.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new solid type. |

---

### `set_state( value )`

Sets the entity state.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `value` | `number` | The new state index. Pass -1 to clear the current state. |

---

### `get_net_number( key )`

Returns the value of a networked number variable.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `key` | `string` | The variable key. |

**Returns** `number` — The stored value, or the default float value if the key does not exist.

---

### `set_net_number( key, value )`

Sets the value of a networked number variable.

Creates the variable if it does not already exist.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `key` | `string` | The variable key. |
| `value` | `number` | The new value. |

---

### `get_net_string( key )`

Returns the value of a networked string variable.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `key` | `string` | The variable key. |

**Returns** `string` — The stored value, or the default string value if the key does not exist.

---

### `set_net_string( key, value )`

Sets the value of a networked string variable.

Creates the variable if it does not already exist.

This property is saved in save files.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `key` | `string` | The variable key. |
| `value` | `string` | The new value. |

---

### `move( velocity, angles )`

Moves the entity by the given velocity and sets its angles.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `velocity` | `LuaVector` | The velocity vector to apply. |
| `angles` | `LuaVector` | The new entity angles. |

---

### `check_client(  )`

Checks the next player in the list for line-of-sight visibility from this entity.

Iterates through all connected players in a round-robin fashion.

**Returns** `LuaValue` — The Lua instance table of the first visible player found, or nil if no player is visible or alive.

---

### `play_sound( filename, channel, volume, attenuation )`

Plays a sound at the entity position.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `filename` | `string` | The sound filename. |
| `channel` | `number` | The audio channel to play on. |
| `volume` | `number` | The playback volume, in the range [0, 1]. |
| `attenuation` | `number` | The distance attenuation factor. |

---

### `parse_origin(  )`

Parses and returns the entity origin from its spawn properties.

**Returns** `LuaVector` — The entity origin as a Lua vector.

---

### `enable_test_flag(  )`

Enables the internal test flag on this entity.

---

### `create( className )`

{: .label .label-blue }
Static

Creates and spawns a new entity with the given class name.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `className` | `string` | The Lua class name of the entity to create. |

**Returns** `GameEntity` — The spawned , or null if not called on the server.

---

### `get_entity_by_classname( className )`

{: .label .label-blue }
Static

Returns the first entity whose class name matches the given value.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `className` | `string` | The class name to search for. |

**Returns** `GameEntity` — The first matching , or null if none is found.

---

### `despawn(  )`

Despawns and removes the entity from the network.

---

### `spawn(  )`

Spawns the entity on the network.

---

### `teleport( origin, angles )`

Teleports the entity to the given origin and sets its angles.

**Parameters**

| Name | Type | Description |
|:-----|:-----|:------------|
| `origin` | `LuaVector` | The new world position as a Lua vector. |
| `angles` | `LuaVector` | The new angles as a Lua vector. |

---

