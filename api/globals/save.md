---
layout: default
title: "save(name)"
parent: globals
grand_parent: API Reference
nav_order: 16
---

# save(name)

Saves the current game state to a named save file.

All entity properties, networked variables, and fields registered via `serialize_field` are written to disk.

**Parameters**
- `name` (`string`) — The save file name.
