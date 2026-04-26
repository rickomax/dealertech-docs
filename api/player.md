# `player`

`player` is the Lua-side class used for player-controlled entities.

In addition to the base `entity` API, `player` exposes view-related helpers and is expected to implement input handling callbacks used by the engine simulation.

`player` inherits everything from [`entity`](entity.md).

---

## Ownership

### `player:is_owner() -> boolean`
Returns whether this player entity is owned by the local client.

---

## View

### `player:get_view_origin() -> vector`
Returns the world position of the player's camera.

**Returns**
- `vector` — Camera world position, or default if not running on the server.

---

### `player:get_view_height() -> number`
Returns the current view height of the player.

### `player:set_view_height(height)`
Sets the view height of the player.

**Parameters**
- `height` (`number`)

**Server-only**

---

### `player:get_view_offset() -> vector`
Returns the view offset of the player relative to its origin.

**Returns**
- `vector` — View offset, or default if not running on the server.

### `player:set_view_offset(offset)`
Sets the view offset of the player relative to its origin.

**Parameters**
- `offset` (`vector`)

**Server-only**

---

### `player:set_view_model(filename)`
Sets the view model displayed in first-person for this player.

**Parameters**
- `filename` (`string`) — MDL filename of the view model.

---

### `player:set_view_frame(name)`
Sets the current animation frame of the player's view model.

**Parameters**
- `name` (`string`) — Animation frame name.

---

### `player:set_third_person(enabled)`
Enables or disables third-person camera mode.

**Parameters**
- `enabled` (`boolean`) — `true` for third-person, `false` for first-person.

**Server-only**

---

## Punch / Roll / Sway

### `player:get_punch_angles() -> vector`
Returns the current punch angles applied to the player's view.

### `player:set_punch_angles(value)`
Sets the punch angles applied to the player's view (e.g. when taking damage).

**Parameters**
- `value` (`vector`) — New punch angles.

---

### `player:set_roll(value)`
Sets the roll angle of the player.

**Parameters**
- `value` (`number`) — Roll angle in degrees.

**Server-only**

---

### `player:set_sway_amount(value)`
Sets the weapon sway amount for this player.

**Parameters**
- `value` (`number`)

**Server-only**

---

### `player:set_weapon_offset(offset)`
Sets the weapon model position offset.

**Parameters**
- `offset` (`vector`)

**Server-only**

---

## Required Lua Callbacks

The engine expects the Lua `player` class table to define the following functions:

### `player.create(self_entity) -> table`
Creates and returns the Lua instance table for the player. Called once when the player spawns.

---

### `player.read_input(self, input_data)`
Reads current input and writes raw values into `input_data`.

**Parameters**
- `self` (`table`) — Player instance table.
- `input_data` (`input_data`) — Output buffer to fill (32 float slots).

---

### `player.process_actions(self, input_data)`
Processes button-style actions (jump, fire, weapon switch, etc.) using the values placed into `input_data`.

**Parameters**
- `self` (`table`) — Player instance table.
- `input_data` (`input_data`)

---

### `player.process_movement(self, input_data, in_move, out_move)`
Processes input and produces the next movement state.

**Parameters**
- `self` (`table`)
- `input_data` (`input_data`)
- `in_move` (`movement_data`) — Current movement state.
- `out_move` (`movement`) — Output movement state to fill.

The engine uses `out_move` to build the next movement packet. Final collision/grounding is applied by the engine after this function returns.

---

### `player.spawn(self)`
Optional. Called when the player entity is (re)spawned on the server.

---

## Example (skeleton)

```lua
player = {}

function player.create(self_entity)
    local self = {}
    -- store references / initialize
    return self
end

function player.read_input(self, input_data)
    input_data[0] = input.read_raw_float("<Keyboard>/w") - input.read_raw_float("<Keyboard>/s")
    input_data[1] = input.read_raw_float("<Keyboard>/d") - input.read_raw_float("<Keyboard>/a")
    input_data[4] = input.is_held("<Keyboard>/space")
end

function player.process_actions(self, input_data)
    if input.was_pressed("<Keyboard>/r") == 1 then
        -- reload
    end
end

function player.process_movement(self, input_data, in_move, out_move)
    out_move.angles      = in_move.angles
    out_move.velocity    = in_move.velocity
    out_move.is_grounded = in_move.is_grounded
    -- apply movement logic using input_data...
end
```
