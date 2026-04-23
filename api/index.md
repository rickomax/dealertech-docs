---
title: API Reference
nav_order: 1
---

# Lua API Reference

Available Lua-exposed objects and globals.

- [`array`](./array.md) — A dynamic, 1-indexed array of Lua values backed by a managed list.
- [`bsp`](./bsp.md) — Provides Lua access to the loaded BSP map, including map discovery and content queries.
- [`config`](./config.md) — Provides Lua access to the persistent configuration store.
- [`console_variable`](./console_variable.md) — Represents a single console variable that can be read from and written to from Lua.
- [`entity`](./entity.md) — Represents entity properties, movement, state, and network variables to Lua scripts.
- [`entity_state`](./entity_state.md) — Represents a single named animation/logic state that an entity can switch to.
- [`font`](./font.md) — Represents a loaded TextMeshPro font asset used by `ui_label` and `ui_input_field`.
- [`input`](./input.md) — Provides access to the input system.
- [`input_data`](./input_data.md) — A fixed-size float buffer used by the input system to pass raw input values.
- [`light`](./light.md) — Represents a networked point light attached to the world or to a parent entity.
- [`lights`](./lights.md) — Provides Lua access to the global light style table and helpers for spawning lights.
- [`math`](./math.md) — Exposes common numeric helpers, trigonometry, and random-number utilities to Lua.
- [`move_type`](./move_type.md) — Integer constants identifying entity movement types.
- [`movement`](./movement.md) — Output movement written by the Lua `process_movement` function each tick.
- [`movement_data`](./movement_data.md) — Input movement snapshot passed into the Lua `process_movement` function each tick.
- [`particles`](./particles.md) — Provides Lua access to the particle system.
- [`physics`](./physics.md) — Provides Lua-exposed physics queries and trace operations.
- [`player`](./player.md) — Represents player-specific Lua bindings for input, movement, camera and view model control.
- [`solid`](./solid.md) — Integer constants identifying entity solid/collision types.
- [`trace_result`](./trace_result.md) — Represents the result of a physics trace query.
- [`ui_image`](./ui_image.md) — Exposes a raw image UI element to Lua.
- [`ui_input_field`](./ui_input_field.md) — Exposes a TextMeshPro single-line input field UI element to Lua.
- [`ui_label`](./ui_label.md) — Exposes a TextMeshPro text label UI element to Lua.
- [`ui_panel`](./ui_panel.md) — Exposes a container UI panel to Lua.
- [`vector`](./vector.md) — A three-component vector object.
- [`vector4`](./vector4.md) — A four-component vector object.
