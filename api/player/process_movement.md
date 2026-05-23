---
layout: default
title: "`player.process_movement(self, input_data, in_move, out_move)`"
parent: player
grand_parent: API Reference
nav_order: 19
---

# `player.process_movement(self, input_data, in_move, out_move)`

Processes input and produces the next movement state.

**Parameters**
- `self` (`table`)
- `input_data` (`input_data`)
- `in_move` (`movement_data`) — Current movement state.
- `out_move` (`movement`) — Output movement state to fill.

The engine uses `out_move` to build the next movement packet. Final collision/grounding is applied by the engine after this function returns.

---
