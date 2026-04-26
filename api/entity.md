---
layout: default
title: entity
parent: API Reference
---
# `entity`

`entity` represents a game entity instance and its Lua-exposed properties, movement, state and networked variables.

It exposes helpers for:
- Reading/writing string properties
- Finding other entities
- Querying and changing transform / movement data
- Managing simple state-machine state (`entity_state`)
- Reading/writing networked numbers, strings and vectors
- Spawning, despawning and teleporting entities
- Basic line-of-sight client checks
- Playing sounds

Most setter functions only have an effect when called on the server (they will do nothing when called on a non-server instance).

---

## Property Access

### `entity[key] : string|nil`
Gets or sets a string property by key.

**Notes**
- Returns `nil` if the key does not exist.
- Values are stored as strings.

---

## Identity

### `entity:get_unique_id() -> integer`
Returns the entity's unique id.

---

## Spawning / Lifecycle

### `entity.create(className) -> table`
Spawns a new entity with the given class name and returns its Lua instance table.

**Parameters**
- `className` (`string`)

**Returns**
- `table` — Lua instance table of the spawned entity, or `nil` if not running on the server.

---

### `entity:spawn()`
Spawns this entity on the network.

**Server-only**
- Has no effect when not running on the server.

---

### `entity:despawn()`
Despawns and removes the entity from the network.

**Server-only**
- Has no effect when not running on the server.

---

### `entity:enable_test_flag()`
Enables an internal test flag on this entity. Used by gameplay diagnostics.

---

## Lookup

### `entity.get_entity_by_classname(className) -> entity|nil`
Returns the first entity whose class name matches `className`.

**Parameters**
- `className` (`string`)

---

### `entity.get_entity_by_unique_id(id) -> entity|nil`
Returns the first entity whose unique id matches `id`.

**Parameters**
- `id` (`integer`)

---

### `entity.get_entity_by_targetname(targetName) -> entity|nil`
Returns the first entity whose `targetname` property matches `targetName`.

**Parameters**
- `targetName` (`string`)

---

## Ownership

### `entity:get_owner() -> table|nil`
Returns the Lua instance table of the entity that owns this entity, or `nil` if no owner is set.

### `entity:set_owner(owner)`
Sets the entity that owns this entity.

**Parameters**
- `owner` (`entity|nil`) — Owner entity, or `nil` to clear ownership.

**Server-only**

---

## Visibility / Targeting

### `entity:check_client() -> table|nil`
Cycles through connected players in round-robin fashion and returns the Lua instance table of the next player that is alive and visible from this entity (line-of-sight check). Returns `nil` if no player matches.

**Server-only**
- Returns `nil` when not running on the server.

---

## Angle / Orientation

### `entity:get_angle() -> number`
Returns the entity yaw angle, in degrees.

### `entity:get_angles() -> vector`
Returns the entity orientation angles (pitch, yaw, roll) as a vector.

### `entity:set_angle(angle)`
Sets the entity yaw angle.

**Parameters**
- `angle` (`number`) — Yaw angle in degrees.

**Server-only**

### `entity:set_angles(angles)`
Sets the entity orientation angles.

**Parameters**
- `angles` (`vector`)

**Server-only**

---

## Position / Size / Velocity

### `entity:get_origin() -> vector`
Returns the current world position.

### `entity:set_origin(origin)`
Sets the entity world position.

**Parameters**
- `origin` (`vector`)

**Server-only**

### `entity:get_velocity() -> vector`
Returns the current velocity.

### `entity:set_size(min, max)`
Sets the entity axis-aligned bounding box.

**Parameters**
- `min` (`vector`) — Minimum corner.
- `max` (`vector`) — Maximum corner.

**Server-only**

### `entity:get_brush_size() -> vector`
Returns the brush size for BSP/brush entities.

**Returns**
- `vector` — Returns a zero vector if the entity solid type is not `solid.bsp`.

### `entity:is_grounded() -> boolean`
Returns whether the entity is currently grounded.

### `entity:parse_origin() -> vector`
Parses the entity origin from its raw spawn `"origin"` property and returns it as a vector.

---

## Movement

### `entity:move(velocity, angles)`
Moves the entity by the given velocity for one simulation step, and updates its angles.

**Parameters**
- `velocity` (`vector`) — Velocity to apply.
- `angles` (`vector|nil`, default `nil`) — Optional new angles. If omitted, the current angles are kept.

**Notes**
- Has no effect when not running on the server.
- Has no effect if the entity move type is `move_type.none` or velocity is zero.
- For BSP-solid entities, the angles input is ignored.

---

### `entity:teleport(origin, angles)`
Teleports the entity to the given world position and orientation.

**Parameters**
- `origin` (`vector`)
- `angles` (`vector`)

---

### `entity:set_move_type(value)`
Sets the entity move type.

**Parameters**
- `value` (`integer`) — A `move_type.*` constant.

**Server-only**

---

### `entity:set_solid(value)`
Sets the entity solid type.

**Parameters**
- `value` (`integer`) — A `solid.*` constant.

**Server-only**

---

## Visuals

### `entity:get_frame() -> string`
Returns the current animation frame name.

### `entity:set_frame(name)`
Sets the entity animation frame.

**Parameters**
- `name` (`string`)

### `entity:get_model() -> string`
Returns the current MDL filename.

### `entity:set_model(filename)`
Sets the entity model.

**Parameters**
- `filename` (`string`)

### `entity:set_skin(index)`
Sets the entity skin.

**Parameters**
- `index` (`integer`)

### `entity:set_label(label)`
Sets the debug label text displayed on the entity.

**Parameters**
- `label` (`string`)

---

## Health

### `entity:get_health() -> number`
Returns the current health value.

### `entity:set_health(value)`
Sets the entity health.

**Parameters**
- `value` (`number`)

**Server-only**

---

## State Machine

### `entity:get_state() -> string`
Returns the current state index, as a string.

### `entity:set_state(stateIndex)`
Assigns the current state index for this entity.

**Parameters**
- `stateIndex` (`integer`) — A state index returned by `entity_state.create`. Pass `-1` to clear the current state.

**Behavior**
- If the new state has a non-empty `frame`, the entity frame is updated immediately.
- If the new state's `interval` is negative, it will not automatically advance.
- Otherwise the state is scheduled to advance after `interval` seconds.

---

## Networked Variables

### `entity:get_net_number(key) -> number`
Returns the value of a networked number variable.

**Parameters**
- `key` (`string`)

### `entity:set_net_number(key, value)`
Sets the value of a networked number variable. Creates the variable if it does not already exist.

**Parameters**
- `key` (`string`)
- `value` (`number`)

**Server-only**

### `entity:get_net_string(key) -> string`
Returns the value of a networked string variable.

### `entity:set_net_string(key, value)`
Sets the value of a networked string variable. Creates the variable if it does not already exist.

**Server-only**

### `entity:get_net_vector(key) -> vector`
Returns the value of a networked vector variable.

### `entity:set_net_vector(key, value)`
Sets the value of a networked vector variable. Creates the variable if it does not already exist.

**Server-only**

---

## Sound

### `entity:play_sound(filename, channel, volume, attenuation)`
Plays a sound at the entity position.

**Parameters**
- `filename` (`string`) — Sound filename.
- `channel` (`integer`) — Audio channel.
- `volume` (`number`) — Volume in `[0, 1]`.
- `attenuation` (`number`) — Distance attenuation factor.
