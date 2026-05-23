---
layout: default
title: "`flag4` : `boolean`"
parent: movement_data
grand_parent: API Reference
nav_order: 9
---

# `flag4` : `boolean`

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
