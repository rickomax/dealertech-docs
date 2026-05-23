---
layout: default
title: "`particles.spawn(filename, origin, duration, count, direction)`"
parent: particles
grand_parent: API Reference
nav_order: 1
---

# `particles.spawn(filename, origin, duration, count, direction)`

Spawns a networked particle effect at the given world position.

**Parameters**
- `filename` (`string`) — The particle effect filename.
- `origin` (`vector`) — World position where the effect is emitted.
- `duration` (`number`) — Lifetime of the effect, in seconds.
- `count` (`integer`) — Number of particles to emit.
- `direction` (`vector|nil`, default zero vector) — Initial emission direction. A zero vector emits in the effect's authored default direction.

**Server-only**
- Has no effect when not running on the server.
