---
layout: default
title: "`entity:check_client() -> table|nil`"
parent: entity
grand_parent: API Reference
nav_order: 14
---

# `entity:check_client() -> table|nil`

Cycles through connected players in round-robin fashion and returns the Lua instance table of the next player that is alive and visible from this entity (line-of-sight check). Returns `nil` if no player matches.

**Server-only**
- Returns `nil` when not running on the server.

---

## Angle / Orientation
