---
layout: default
title: "bsp.change_map(filename)"
parent: bsp
grand_parent: API Reference
nav_order: 5
---

# `bsp.change_map(filename)`

Makes a BSP file the active map on this machine, like Quake's `map` console command - parsing it first if it wasn't already cached via `bsp.precache`/`load_bsp`.

Unlike the top-level `map` global, this is local only - it does not network-sync the change to other clients.

**Parameters**
- `filename` (`string`) — BSP filename, relative to the `maps` folder.
