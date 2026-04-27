# `movement_data` / `movement`

The engine exposes two related Lua types used by the player movement pipeline:

- `movement_data` — the **input** movement state passed to `process_movement`.
- `movement` — the **output** movement state filled by `process_movement` and read back by the engine.

Both contain orientation, velocity, grounded state and a set of user-defined flags.

---

## `movement_data`

Passed to `player.process_movement(self, input_data, in_move, out_move)` as `in_move`.

### Fields

| Field           | Type      | Description                                              |
|-----------------|-----------|----------------------------------------------------------|
| `angles`        | `vector`  | Current orientation angles.                              |
| `position`      | `vector`  | Current world position.                                  |
| `velocity`      | `vector`  | Current movement velocity.                               |
| `is_grounded`   | `boolean` | Whether the entity is currently grounded.                |
| `was_grounded`  | `boolean` | Whether the entity was grounded on the previous tick.    |
| `flag1`–`flag4` | `boolean` | User-defined boolean flags carried through the packet.   |

---

## `movement`

Passed to `player.process_movement(self, input_data, in_move, out_move)` as `out_move`.

The engine reads these fields after your callback returns to build the next movement packet.

### Fields

| Field           | Type      | Description                                              |
|-----------------|-----------|----------------------------------------------------------|
| `angles`        | `vector`  | New orientation angles to apply.                         |
| `velocity`      | `vector`  | New movement velocity to apply.                          |
| `is_grounded`   | `boolean` | Whether the entity should be considered grounded.        |
| `flag1`–`flag4` | `boolean` | User-defined boolean flags forwarded to the simulation.  |

> Note: `movement` does not have a `position` field — the engine derives it from the resulting collision step.

---

## Example

```lua
function player.process_movement(self, input_data, in_move, out_move)
    -- Start from the current state
    out_move.angles      = in_move.angles
    out_move.velocity    = in_move.velocity
    out_move.is_grounded = in_move.is_grounded

    -- Apply input
    local fwd  = input_data[0]
    local side = input_data[1]
    out_move.velocity = vector.create(fwd * 200, side * 200, in_move.velocity.z)

    -- Carry "is_crouching" flag through
    out_move.flag1 = in_move.flag1
end
```
