---
layout: default
title: "entity:set_model(filename)"
parent: entity
grand_parent: API Reference
nav_order: 40
---

# `entity:set_model(filename)`

Sets the entity model.

Accepts `.mdl` files as well as `.bsp` files. When given a `.bsp` file, the
entity model is the first model in the BSP file's models lump, parsed and
cached automatically the first time it's used - no precache step is needed.
A BSP model is drawn the same way as a map's own BSP submodels rather than
through a regular animated model, with bounding-box collision derived from
the model's own bounds (like a `.mdl` entity's, not per-triangle).

**Parameters**
- `filename` (`string`)

