---
layout: default
title: "`entity:get_net_table(key) -> any`"
parent: entity
grand_parent: API Reference
nav_order: 57
---

# `entity:get_net_table(key) -> any`

Returns the value of a networked table variable. The stored Lua source string is deserialized back into a Lua value.

**Parameters**
- `key` (`string`)

**Returns**
- The deserialized Lua value, or `nil` if the key does not exist.
