---
layout: default
title: "player:broadcast(table, destination_function)"
parent: player
grand_parent: API Reference
nav_order: 22
---

# `player:broadcast(table, destination_function)`

Serializes a table and calls the named function on this player's Lua instance on the server
and every client.

**Parameters**
- `table` (`table`) - follows the Lua serializer rules
- `destination_function` (`string`) - the instance function to call on the receiving side

**Server-only**
