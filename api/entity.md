---
layout: default
title: entity
parent: API Reference
---

# `entity`

Represents entity properties, movement, state, and network variables to Lua scripts.

**C# type:** `GameEntity`  

**Source:** `Assets/DealerTech/Runtime/Entities/GameEntity/GameEntityLua.cs`

## Members

### `indexer`

Gets or sets a property value by key.

`public string this[string key]`

### `get_unique_id`

Returns the entity unique ID.

`public int GetUniqueId()`

### `get_velocity`

Returns the current velocity of the entity.

`public LuaVector GetVelocity()`

### `get_angle`

Returns the current yaw angle of the entity.

`public float GetAngle()`

### `get_angles`

Returns the current angles of the entity.

`public LuaVector GetAngles()`

### `get_brush_size`

Returns the brush size of the entity.

`public LuaVector GetBrushSize()`

### `get_frame`

Returns the current animation frame name of the entity.

`public string GetFrame()`

### `get_health`

Returns the current health of the entity.

`public float GetHealth()`

### `get_model`

Returns the current model filename of the entity.

`public string GetModel()`

### `get_origin`

Returns the current origin of the entity.

`public LuaVector GetOrigin()`

### `get_state`

Returns the current state index of the entity.

`public string GetState()`

### `is_grounded`

Returns whether the entity is grounded.

`public bool IsGrounded()`

### `set_angle`

Sets the entity yaw angle.

`public void SetAngle(float value)`

### `set_angles`

Sets the entity pitch, yaw and roll angles.

`public void SetAngles(LuaVector angles)`

### `set_frame`

Sets the entity animation frame.

`public void SetFrame(string name)`

### `set_skin`

Sets the entity skin.

`public void SetSkin(int skinIndex)`

### `set_health`

Sets the entity health.

`public void SetHealth(float value)`

### `set_label`

Sets the debug label text displayed on the entity.

`public void SetLabel(string label)`

### `set_model`

Sets the entity model.

`public void SetModel(string filename)`

### `set_move_type`

Sets the entity move type.

`public void SetMoveType(int value)`

### `set_origin`

Sets the entity origin.

`public void SetOrigin(LuaVector origin)`

### `set_size`

Sets the entity axis-aligned bounding box.

`public void SetSize(LuaVector min, LuaVector max)`

### `set_solid`

Sets the entity solid type.

`public void SetSolid(int value)`

### `set_state`

Sets the entity state.

`public void SetState(int value)`

### `get_net_number`

Returns the value of a networked number variable.

`public float GetNetworkNumber(string key)`

### `set_net_number`

Sets the value of a networked number variable. Creates the variable if it does not already exist.

`public void SetNetworkNumber(string key, float value)`

### `get_net_string`

Returns the value of a networked string variable.

`public string GetNetworkString(string key)`

### `set_net_string`

Sets the value of a networked string variable. Creates the variable if it does not already exist.

`public void SetNetworkString(string key, string value)`

### `move`

Moves the entity by the given velocity and sets its angles.

`public void Move(LuaVector velocity, LuaVector angles)`

### `check_client`

Checks the next player in the list for line-of-sight visibility from this entity. Iterates through all connected players in a round-robin fashion.

`public LuaValue CheckClient()`

### `play_sound`

Plays a sound at the entity position.

`public void PlaySound(string filename, int channel, float volume, float attenuation)`

### `parse_origin`

Parses and returns the entity origin from its spawn properties.

`public LuaVector ParseOrigin()`

### `enable_test_flag`

Enables the internal test flag on this entity.

`public void EnableTestFlag()`

### `create`

Creates and spawns a new entity with the given class name.

`public static GameEntity Create(string className)`

### `get_entity_by_classname`

Returns the first entity whose class name matches the given value.

`public static GameEntity GetGameEntityByClassName(string className)`

### `get_entity_by_unique_id`

Returns the first entity whose unique id matches the given value.

`public static GameEntity GetGameEntityByUniqueId(int uniqueId)`

### `get_entity_by_targetname`

Returns the first entity whose `targetname` property matches the given value.

`public static GameEntity GetEntityByTargetName(string className)`

### `despawn`

Despawns and removes the entity from the network.

`public virtual void Despawn()`

### `spawn`

Spawns the entity on the network.

`public virtual void Spawn()`

### `teleport`

Teleports the entity to the given origin and sets its angles.

`public void Teleport(LuaVector origin, LuaVector angles)`
