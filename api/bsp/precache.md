---
layout: default
title: "bsp.precache(filename)"
parent: bsp
grand_parent: API Reference
nav_order: 4
---

# `bsp.precache(filename)`

Parses a BSP file and caches it, without making it the active map. A no-op if the file was already cached. Equivalent to the top-level `load_bsp` global.

**Parameters**
- `filename` (`string`) — BSP filename, relative to the `maps` folder.
