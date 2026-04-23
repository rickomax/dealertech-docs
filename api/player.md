---
layout: default
title: player
parent: API Reference
---

# `player`

Represents player-specific Lua bindings for input, movement, camera and view model control.

**C# type:** `GamePlayer`  

**Source:** `Assets/DealerTech/Runtime/Entities/GamePlayer/GamePlayerLua.cs`

## Members

### `is_owner`

Returns whether this player entity is owned by the local client.

`public bool LuaIsOwner()`

### `get_punch_angles`

Returns the current punch angles applied to the player's view.

`public LuaVector GetPunchAngles()`

### `get_view_height`

Returns the current view height of the player.

`public float GetViewHeight()`

### `get_view_offset`

Returns the view offset of the player relative to its origin.

`public LuaVector GetViewOffset()`

### `get_view_origin`

Returns the world position of the player's camera.

`public LuaVector GetViewOrigin()`

### `set_punch_angles`

Sets the punch angles applied to the player's view.

`public void SetPunchAngles(LuaVector value)`

### `set_roll`

Sets the roll angle of the player.

`public void SetRoll(float value)`

### `set_sway_amount`

Sets the weapon sway amount for this player.

`public void SetSwayAmount(float value)`

### `set_third_person`

Enables or disables third-person camera mode for this player.

`public void SetThirdPerson(bool value)`

### `set_view_frame`

Sets the current animation frame of the player's view model.

`public void SetViewFrame(string name)`

### `set_view_height`

Sets the view height of the player.

`public void SetViewHeight(float height)`

### `set_view_model`

Sets the view model displayed in first-person for this player.

`public void SetViewModel(string filename)`

### `set_view_offset`

Sets the view offset of the player relative to its origin.

`public void SetViewOffset(LuaVector offset)`

### `set_weapon_offset`

Sets the weapon model position offset.

`public void SetWeaponOffset(LuaVector offset)`
