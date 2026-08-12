---
layout: default
title: "load_bsp_model(filename)"
parent: globals
grand_parent: API Reference
nav_order: 2
---

# load_bsp_model(filename)

Parses a BSP file as an entity model and caches it. A no-op if the model was already cached.

This is the loader for brush models that entities wear through `entity:set_model()`, such as the health and ammo boxes, as opposed to `load_bsp`, which precaches a playable map. Only the first model in the file is used, and the file is read from the `models` folder rather than `maps`.

**Parameters**
- `filename` (`string`) — BSP filename including extension, relative to the `models` folder (e.g. `"b_bh25.bsp"`).

**Errors**
- Throws if the file does not exist.
