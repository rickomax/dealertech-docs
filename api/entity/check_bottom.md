---
layout: default
title: "entity:check_bottom()"
parent: entity
grand_parent: API Reference
nav_order: 83
---

# `entity:check_bottom()`

Checks whether the entity is standing on solid ground. All four corners of its bounding box
bottom must have ground directly beneath them; when they do not, the check passes as long as
ground exists within two step heights below the center and no corner's ground sits more than
one step height below it.

**Returns**
- `boolean` - whether the entity stands on acceptable ground

**Server-only** (returns `false` otherwise)
