---
layout: default
title: "load_bsp(filename)"
parent: globals
grand_parent: API Reference
nav_order: 1
---

# load_bsp(filename)

Parses a BSP file and caches it, without making it the active map. A no-op if the file was already cached.

Use `map` afterwards to actually switch to it - precaching first avoids re-parsing the file when you do.

**Parameters**
- `filename` (`string`) — BSP filename without extension, relative to the `maps` folder (e.g. `"e1m1"`).
