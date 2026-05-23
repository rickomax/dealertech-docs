---
layout: default
title: "entity:set_net_table(key, value)"
parent: entity
grand_parent: API Reference
nav_order: 58
---

# `entity:set_net_table(key, value)`

Sets the value of a networked table variable. The value is serialized to a Lua source string and stored in the underlying networked string slot. Creates the variable if it does not already exist.

**Parameters**
- `key` (`string`)
- `value` (`any`) — Tables and primitives are supported. Functions, userdata and shared/cyclic references follow the engine's serializer rules.

**Server-only**

