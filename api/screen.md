---
layout: default
title: screen
parent: API Reference
---
# `screen`

`screen` provides Lua-exposed control over fullscreen visual effects.

All functions are static and accessed directly from the `screen` table.

---

## Functions

### `screen.play_effect(filename, duration)`
Plays a fullscreen visual effect for the given duration.

**Parameters**
- `filename` (`string`) — The screen effect filename.
- `duration` (`number`) — Effect duration, in seconds.

---

### `screen.stop_effects()`
Stops all currently playing fullscreen effects.
