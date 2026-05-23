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

### `entity[key]`
Gets or sets a spawn property by key.

**Notes**
- Returns `nil` if the key does not exist.
- Values are stored internally as strings. When a key has been registered with a
  typed accessor (see `entity.register_type`), the raw value is parsed into the
  configured type when read.
- The keys `origin`, `angle` and `spawnflags` are pre-registered as `vector`,
  `number` and `number` respectively.
- When writing, the assigned value is converted back to a string via `tostring`.

---

### `entity.register_type(name, type)`
Registers a typed accessor for an entity property key. Subsequent reads through
`entity[key]` parse the raw string value into the configured type rather than
returning it as a string.

**Parameters**
- `name` (`string`) — The property key.
- `type` (`string`) — The target type identifier. Supported values:
  - `"float"` — Parsed as a number. Returns `0` if parsing fails.
  - `"vector"` — Parsed as a `vector`.
  - Any other value falls back to returning the raw string.

**Notes**
- The keys `origin`, `angle` and `spawnflags` are pre-registered as `vector`,
  `float` and `float` respectively.

---

## Identity

### `entity:get_instance_id() -> integer`
Returns the entity's unique instance id.

### `entity:get_table() -> table`
Returns the Lua instance table associated with this entity.

---

## Spawning / Lifecycle

### `entity.create(className, origin, angles) -> table`
Spawns a new entity with the given class name and returns its Lua instance table.

**Parameters**
- `className` (`string`) — The entity class name.
- `origin` (`vector|nil`, default zero vector) — Initial world position.
- `angles` (`vector|nil`, default zero vector) — Initial pitch, yaw and roll angles.

**Returns**
- `table` — Lua instance table of the spawned entity, or `nil` if not running on the server.

---

### `entity:spawn(delay)`
Spawns this entity on the network, optionally after a delay.

**Parameters**
- `delay` (`number|nil`, default `0`) — Delay in seconds before spawn. `0` or negative spawns immediately.

**Returns**
- `boolean` — `true` if a delayed spawn was scheduled, `false` if spawned immediately or the call was ignored.

**Server-only**
- Has no effect when not running on the server.

---

### `entity:despawn(delay)`
Despawns and removes the entity from the network, optionally after a delay.

**Parameters**
- `delay` (`number|nil`, default `0`) — Delay in seconds before despawn. `0` or negative despawns immediately.

**Returns**
- `boolean` — `true` if a delayed despawn was scheduled, `false` if despawned immediately or the call was ignored.

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

### `entity:get_size(min, max)`
Returns the entity axis-aligned bounding box corners via output parameters.

**Parameters**
- `min` (`vector`, out) — Receives the minimum corner.
- `max` (`vector`, out) — Receives the maximum corner.

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

### `entity:add_force_velocity(force)`
Applies an instantaneous velocity change to the entity's rigid body.

**Parameters**
- `force` (`vector`) — Velocity change to add, in world coordinates.

**Notes**
- Has no effect when not running on the server.
- Has no effect unless the entity move type is `move_type.physics`.

---

### `entity:get_move_type() -> integer`
Returns the entity move type as a `move_type.*` constant.

### `entity:set_move_type(value)`
Sets the entity move type.

**Parameters**
- `value` (`integer`) — A `move_type.*` constant.

**Server-only**

---

### `entity:get_solid() -> integer`
Returns the entity solid type as a `solid.*` constant.

### `entity:set_solid(value)`
Sets the entity solid type.

**Parameters**
- `value` (`integer`) — A `solid.*` constant.

**Server-only**

---

### `entity:get_yaw_speed() -> number`
Returns the entity yaw rotation speed, in degrees per second.

### `entity:set_yaw_speed(speed)`
Sets the entity yaw rotation speed.

**Parameters**
- `speed` (`number`) — Yaw speed in degrees per second.

**Server-only**

---

## Visuals

### `entity:get_frame_index() -> integer`
Returns the current animation frame index.

The returned index is 1-based, or `0` if no frame is set.

### `entity:get_frame() -> integer`
Returns the current animation frame index.

### `entity:set_frame(value)`
Sets the entity animation frame.

**Parameters**
- `value` (`string|number`) — Frame name (for models with named frames) or 1-based frame index.

### `entity:get_model() -> string`
Returns the current MDL filename.

### `entity:set_model(filename)`
Sets the entity model.

**Parameters**
- `filename` (`string`)

### `entity:get_model_index() -> integer`
Returns the current model index.

### `entity:set_model_index(index)`
Sets the entity model by index.

**Parameters**
- `index` (`integer`) — Model index.

### `entity:get_sprite_index() -> integer`
Returns the current sprite index.

### `entity:set_sprite_index(index)`
Sets the entity sprite by index.

**Parameters**
- `index` (`integer`) — Sprite index.

### `entity:get_skin() -> integer`
Returns the entity's current 1-based skin index.

### `entity:set_skin(index)`
Sets the entity skin.

**Parameters**
- `index` (`integer`) — 1-based skin index.

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

### `entity:get_net_table(key) -> any`
Returns the value of a networked table variable. The stored Lua source string is deserialized back into a Lua value.

**Parameters**
- `key` (`string`)

**Returns**
- The deserialized Lua value, or `nil` if the key does not exist.

### `entity:set_net_table(key, value)`
Sets the value of a networked table variable. The value is serialized to a Lua source string and stored in the underlying networked string slot. Creates the variable if it does not already exist.

**Parameters**
- `key` (`string`)
- `value` (`any`) — Tables and primitives are supported. Functions, userdata and shared/cyclic references follow the engine's serializer rules.

**Server-only**

### `entity:get_net_entity(key) -> entity|nil`
Returns the entity referenced by a networked entity variable, or `nil` if the key does not exist or the referenced entity could not be found.

**Parameters**
- `key` (`string`)

### `entity:set_net_entity(key, value)`
Sets the entity referenced by a networked entity variable. Creates the variable if it does not already exist. Pass `nil` to clear the reference.

**Parameters**
- `key` (`string`)
- `value` (`entity|nil`)

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
