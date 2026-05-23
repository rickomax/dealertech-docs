---
layout: default
title: movement
parent: API Reference
has_children: true
nav_order: 14
---

# `movement`

`movement` is the output movement state written by the Lua `process_movement` function each tick. The engine reads these fields after the callback returns to build the next movement packet.

Passed to `player.process_movement(self, input_data, in_move, out_move)` as `out_move`.

> Note: `movement` does not have a `position` field — the engine derives it from the resulting collision step.
