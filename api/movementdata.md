---
layout: default
title: movement_data
parent: API Reference
---

# `movement_data`

`movement_data` is the input movement snapshot passed into the Lua `process_movement` function each tick.

Passed to `player.process_movement(self, input_data, in_move, out_move)` as `in_move`.

---

## Fields

### `angles` : `vector`
Current orientation angles.

### `position` : `vector`
Current world position.

### `velocity` : `vector`
Current movement velocity.

### `is_grounded` : `boolean`
Whether the entity is currently grounded.

### `was_grounded` : `boolean` *(deprecated)*
Whether the entity was grounded on the previous tick.

### `flag1` : `boolean`
User-defined boolean flag carried through the packet.

### `flag2` : `boolean`
User-defined boolean flag carried through the packet.

### `flag3` : `boolean`
User-defined boolean flag carried through the packet.

### `flag4` : `boolean`
User-defined boolean flag carried through the packet.

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
