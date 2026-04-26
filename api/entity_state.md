# `entity_state`

`entity_state` represents a single state entry used by the engine's entity state machine.

Each state defines:
- The animation frame to use.
- The duration of the state.
- Optional Lua code to execute when the state runs.

---

## Fields

### `frame` : `string`
Name of the animation frame associated with this state.

---

### `interval` : `number`
Duration (in seconds) that the entity remains in this state before advancing.

---

### `code` : `LuaValue`
Lua function or value executed when the state is processed.

Typically this is a function containing the logic to run during this state.

---

## Creation

### `entity_state.create(frame, interval, code) -> entity_state`

Creates a new entity state instance.

**Parameters**
- `frame` (`string`) — Animation frame name.
- `interval` (`number`) — Duration in seconds.
- `code` (`LuaValue`) — Lua function or value to execute for this state.

**Returns**
- `entity_state`

---

## Example

```lua
local state = entity_state.create(
    "walk_01",
    0.1,
    function(self)
        self:move_forward()
    end
)
```
