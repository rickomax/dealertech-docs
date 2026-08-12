---
layout: default
title: "entity:set_size(min, max)"
parent: entity
grand_parent: API Reference
nav_order: 23
---

# `entity:set_size(min, max)`

Sets the entity axis-aligned bounding box.

The corners are relative to the entity origin and use the same coordinate mapping as `entity:get_origin()`. The box does not need to be centred on the origin; `entity:get_size()` returns the same pair back.

**Parameters**
- `min` (`vector`) — Minimum corner.
- `max` (`vector`) — Maximum corner.

**Server-only**

