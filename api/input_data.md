---
layout: default
title: input_data
parent: API Reference
has_children: true
nav_order: 10
---

# `input_data`

`input_data` is a fixed-size float buffer used by the input system to pass raw input values between the engine and Lua.

Each slot corresponds to one input axis or button value, stored as a float. There are **32 available slots** (indexed `0` through `31`).

An `input_data` instance is passed to the player Lua callbacks `read_input` and `process_actions` each frame, and again to `process_movement` so movement code can react to the same inputs.
