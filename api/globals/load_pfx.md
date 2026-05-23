---
layout: default
title: "load_pfx(filename)"
parent: globals
grand_parent: API Reference
nav_order: 6
---

# load_pfx(filename)

Precaches a particle effect file so it can be spawned via `particles.spawn`.

Parses the PFX script format (start/update instruction programs) and stores the compiled instructions in the resource cache. Subsequent calls with the same filename are ignored.

**Parameters**
- `filename` (`string`) — PFX filename relative to the `effects` folder (e.g. `"explosion.pfx"`).

**Errors**
- Throws if the file is not found.
