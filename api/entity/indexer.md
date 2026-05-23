---
layout: default
title: "entity[key]"
parent: entity
grand_parent: API Reference
nav_order: 1
---

# `entity[key]`

Gets or sets a spawn property by key.

**Notes**
- Returns `nil` if the key does not exist.
- Values are stored internally as strings. When a key has been registered with a
  typed accessor (see `entity.register_type`), the raw value is parsed into the
  configured type when read.
- The keys `origin`, `angle` and `spawnflags` are pre-registered as `vector`,
  `number` and `number` respectively.
- When writing, the assigned value is converted back to a string via `tostring`.

