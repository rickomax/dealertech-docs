---
layout: default
title: "`entity.register_type(name, type)`"
parent: entity
grand_parent: API Reference
nav_order: 2
---

# `entity.register_type(name, type)`

Registers a typed accessor for an entity property key. Subsequent reads through
`entity[key]` parse the raw string value into the configured type rather than
returning it as a string.

**Parameters**
- `name` (`string`) — The property key.
- `type` (`string`) — The target type identifier. Supported values:
  - `"float"` — Parsed as a number. Returns `0` if parsing fails.
  - `"vector"` — Parsed as a `vector`.
  - Any other value falls back to returning the raw string.

**Notes**
- The keys `origin`, `angle` and `spawnflags` are pre-registered as `vector`,
  `float` and `float` respectively.

---

## Identity
