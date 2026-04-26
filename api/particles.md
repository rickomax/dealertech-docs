---
layout: default
title: particles
parent: API Reference
---
# `particles`

`particles` provides Lua-exposed particle spawning.

All functions are static and accessed directly from the `particles` table.

All functions only have an effect when called on the server.

---

## Functions

### `particles.spawn(filename, origin, duration, count)`
Spawns a networked particle effect at the given world position.

**Parameters**
- `filename` (`string`) — The particle effect filename.
- `origin` (`vector`) — World position where the effect is emitted.
- `duration` (`number`) — Lifetime of the effect, in seconds.
- `count` (`integer`) — Number of particles to emit.

**Server-only**
- Has no effect when not running on the server.
