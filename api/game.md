---
layout: default
title: game
parent: API Reference
has_children: true
nav_order: 7
---

# `game`

`game` provides Lua access to the global game session state, including the
current skill level, the active game type, and the game name.

All values are networked from the server to all clients. The setter functions
only have an effect when called on the server.
