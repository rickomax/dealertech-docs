---
layout: default
title: player
parent: API Reference
has_children: true
nav_order: 18
---

# `player`

`player` is the Lua-side class used for player-controlled entities.

In addition to the base `entity` API, `player` exposes view-related helpers and is expected to implement input handling callbacks used by the engine simulation.

`player` inherits everything from [`entity`](entity.md).
