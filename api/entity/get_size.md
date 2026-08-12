---
layout: default
title: "entity:get_size(min, max)"
parent: entity
grand_parent: API Reference
nav_order: 22
---

# `entity:get_size(min, max)`

Returns the entity axis-aligned bounding box corners via output parameters.

The corners are relative to the entity origin and use the same coordinate mapping as `entity:get_origin()`, so `get_origin() + min` and `get_origin() + max` give the same box as `entity:get_world_bounds()`.

**Parameters**
- `min` (`vector`, out) — Receives the minimum corner.
- `max` (`vector`, out) — Receives the maximum corner.

