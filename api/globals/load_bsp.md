---
layout: default
title: "load_bsp(filename)"
parent: globals
grand_parent: API Reference
nav_order: 1
---

# load_bsp(filename)

Loads and activates a BSP map file.

Parses the binary BSP data, builds world geometry with lightmaps, creates collision volumes, and spawns all map entities defined in the BSP entity lump.

**Parameters**
- `filename` (`string`) — BSP filename without extension, relative to the `maps` folder (e.g. `"e1m1"`).

**Notes**
- Only one BSP can be loaded at a time.
- After loading completes, the engine calls the `BSPLoaded()` Lua callback if defined.
