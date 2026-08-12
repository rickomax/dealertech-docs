---
layout: default
title: "player:client_command(table, destination_function)"
parent: player
grand_parent: API Reference
nav_order: 21
---

# `player:client_command(table, destination_function)`

Serializes a table and calls the named function on this player's Lua instance on every client.

**Parameters**
- `table` (`table`) - follows the Lua serializer rules; functions, userdata and cyclic
  references are not supported
- `destination_function` (`string`) - the instance function to call on the receiving side

**Server-only**
