---
layout: default
title: "entity:get_alt_texture() -> boolean"
parent: entity
grand_parent: API Reference
nav_order: 75
---

# `entity:get_alt_texture() -> boolean`

Returns whether the entity BSP model is rendering its alternate texture animation.

**Returns**
- `boolean` — `true` when the alternate animation (`+a`..`+j`) is selected, `false` when the regular one (`+0`..`+9`) is.

**Notes**
- Readable on both the server and clients.
- Reflects what was requested through `entity:set_alt_texture(value)`, even when the model has no alternate frames to show.
