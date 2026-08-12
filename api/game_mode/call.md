---
layout: default
title: "game_mode(class_name)"
parent: game_mode
grand_parent: API Reference
nav_order: 2
---

# `game_mode(class_name)`

Shorthand for `game_mode.create`.

**Parameters**
- `class_name` (`string`) - the global Lua table holding the mode's `create` function

**Returns**
- `table` - the mode's Lua instance table, or `nil` when not running on the server

**Server-only**
