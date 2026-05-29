---
layout: default
title: "entity:set_owner(owner)"
parent: entity
grand_parent: API Reference
nav_order: 13
---

# `entity:set_owner(owner)`

Sets the entity that owns this entity.

**Parameters**
- `owner` (`entity|nil`) — Owner entity, or `nil` to clear ownership.

> **Note:** `owner` must be the **native entity representation** (the value handed to you by the engine, e.g. from a lookup/spawn call), **not** the Lua class table that wraps it. Passing the class table instead of the native entity will not set ownership correctly.

**Server-only**

