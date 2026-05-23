---
layout: default
title: "load_mdl(filename)"
parent: globals
grand_parent: API Reference
nav_order: 2
---

# load_mdl(filename)

Precaches a model file so it can be used by entities.

Parses the MDL format, extracts skins, animation frames, and vertex data, and stores the result in the resource cache. Subsequent calls with the same filename are ignored.

**Parameters**
- `filename` (`string`) — MDL filename relative to the `models` folder (e.g. `"player.mdl"`).

**Errors**
- Throws if the file is not found.
