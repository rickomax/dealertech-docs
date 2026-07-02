---
layout: default
title: "map(filename)"
parent: globals
grand_parent: API Reference
nav_order: 20
---

# map(filename)

Makes a BSP file the active map, network-synced to every connected client.

Parses the binary BSP data, builds world geometry with lightmaps, creates collision volumes, and spawns all map entities defined in the BSP entity lump. Reuses the parse from `load_bsp` if it was already called for this file, avoiding a redundant re-parse.

**Parameters**
- `filename` (`string`) — BSP filename without extension, relative to the `maps` folder (e.g. `"e1m1"`).

**Notes**
- Only one BSP can be the active map at a time.
- After loading completes, the engine calls the `BSPLoaded()` Lua callback if defined.
