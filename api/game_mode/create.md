---
layout: default
title: "game_mode.create(class_name)"
parent: game_mode
grand_parent: API Reference
nav_order: 1
---

# `game_mode.create(class_name)`

Spawns a game mode from the given Lua class and returns its instance table. The mode is not
made current; call `set_current` on it for that.

**Parameters**
- `class_name` (`string`) - the global Lua table holding the mode's `create` function

**Returns**
- `table` - the mode's Lua instance table, or `nil` when not running on the server

**Server-only**
