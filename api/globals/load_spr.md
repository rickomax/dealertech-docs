---
layout: default
title: "load_spr(filename)"
parent: globals
grand_parent: API Reference
nav_order: 3
---

# load_spr(filename)

Precaches a sprite file so it can be used by entities.

Parses the SPR format, extracts frame data and timing, and stores the result in the resource cache. Subsequent calls with the same filename are ignored.

**Parameters**
- `filename` (`string`) — SPR filename relative to the `sprites` folder (e.g. `"s_explod.spr"`).

**Errors**
- Throws if the file is not found.
