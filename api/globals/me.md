---
layout: default
title: "me : table"
parent: globals
grand_parent: API Reference
nav_order: 14
---

# me : table

The Lua instance table of the local player.

Set automatically after the player entity spawns. On the server, `me` refers to the host's player. On a client, it refers to that client's own player.

Returns `nil` before the player has spawned.
