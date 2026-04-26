# `input_data`

`input_data` is a fixed-size float buffer used by the input system to pass raw input values between the engine and Lua.

Each slot corresponds to one input axis or button value, stored as a float. There are **32 available slots** (indexed `0` through `31`).

An `input_data` instance is passed to the player Lua callbacks `read_input` and `process_actions` each frame, and again to `process_movement` so movement code can react to the same inputs.

---

## Indexer

### `input_data[index]` : `number`
Gets or sets the raw float input value at the given index.

**Parameters**
- `index` (`integer`) — The 0-based index of the input slot to access.

---

## Conventions

The exact meaning of each slot is decided by your `read_input` implementation. A common layout is:

| Index | Meaning              |
|-------|----------------------|
| 0     | Move forward (–back) |
| 1     | Strafe right (–left) |
| 2     | Yaw delta            |
| 3     | Pitch delta          |
| 4     | Jump (held)          |
| 5     | Fire (held)          |
| ...   | game-specific        |

---

## Example

```lua
function player.read_input(self, input_data)
    input_data[0] = input.read_raw_float("<Keyboard>/w") - input.read_raw_float("<Keyboard>/s")
    input_data[1] = input.read_raw_float("<Keyboard>/d") - input.read_raw_float("<Keyboard>/a")
    input_data[4] = input.is_held("<Keyboard>/space")
end

function player.process_movement(self, input_data, in_move, out_move)
    local fwd = input_data[0]
    local side = input_data[1]
    -- ...
end
```
