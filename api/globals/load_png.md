---
layout: default
title: "load_png(filename)"
parent: globals
grand_parent: API Reference
nav_order: 5
---

# load_png(filename)

Precaches an image file so it can be used by UI elements.

Loads the PNG into a texture with point filtering and clamp wrapping, and stores it in the resource cache. Subsequent calls with the same filename are ignored.

**Parameters**
- `filename` (`string`) — PNG filename relative to the `images` folder (e.g. `"crosshair.png"`).

**Errors**
- Throws if the file is not found.
