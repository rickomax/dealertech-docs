---
layout: default
title: API Reference
nav_order: 2
has_children: true
---

# API Reference

All classes exposed to Lua scripts.

| Class | Summary |
|:------|:--------|
| [`array`](array.html) | A dynamic, 1-indexed array of Lua values backed by a managed list. |
| [`bsp`](bsp.html) | Provides Lua access to the loaded BSP map, including map discovery and content queries. |
| [`config`](config.html) | Provides Lua access to the persistent configuration store. |
| [`entity`](entity.html) | Represents entity properties, movement, state, and network variables to Lua scripts. |
| [`entity_state`](entity_state.html) | Represents a single named animation/logic state that an entity can switch to. |
| [`font`](font.html) | Represents a loaded TextMeshPro font asset used by `ui_label` and `ui_input_field`. |
| [`game`](game.html) | Provides Lua access to the global game session state (skill level, game type and game name). |
| [`globals`](globals.html) | Lua globals registered in `LuaInterface.SetupEnvironment`. |
| [`input`](input.html) | Provides access to the input system. |
| [`input_data`](input_data.html) | A fixed-size float buffer used by the input system to pass raw input values. |
| [`light_source`](light_source.html) | Represents a networked dynamic light and provides BSP light style helpers. |
| [`math`](math.html) | Exposes common numeric helpers, trigonometry, and random-number utilities to Lua. |
| [`move_type`](move_type.html) | Integer constants identifying entity movement types. |
| [`movement`](movement.html) | Output movement written by the Lua `process_movement` function each tick. |
| [`movement_data`](movement_data.html) | Input movement snapshot passed into the Lua `process_movement` function each tick. |
| [`particles`](particles.html) | Provides Lua access to the particle system. |
| [`physics`](physics.html) | Provides Lua-exposed physics queries and trace operations. |
| [`player`](player.html) | Represents player-specific Lua bindings for input, movement, camera and view model control. |
| [`screen`](screen.html) | Provides Lua-exposed control over fullscreen visual effects. |
| [`solid`](solid.html) | Integer constants identifying entity solid/collision types. |
| [`trace_result`](trace_result.html) | Represents the result of a physics trace query. |
| [`ui_element`](ui_element.html) | Base class shared by all UI elements exposed to Lua. |
| [`ui_image`](ui_image.html) | Exposes a raw image UI element to Lua. |
| [`ui_input_field`](ui_input_field.html) | Exposes a TextMeshPro single-line input field UI element to Lua. |
| [`ui_label`](ui_label.html) | Exposes a TextMeshPro text label UI element to Lua. |
| [`ui_panel`](ui_panel.html) | Exposes a container UI panel to Lua. |
| [`vector`](vector.html) | A three-component vector object. |
| [`vector4`](vector4.html) | A four-component vector object. |
