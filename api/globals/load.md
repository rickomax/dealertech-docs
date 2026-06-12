---
layout: default
title: "load(name)"
parent: globals
grand_parent: API Reference
nav_order: 17
---

# load(name)

Loads a previously saved game state from a named save file.

The session is fully restarted — the scene is reloaded, a new host session is started, and the save is applied to it. All entity properties, networked variables, and fields registered via `serialize_field` are restored.

**Parameters**
- `name` (`string`) — The save file name.

Throws `invalid_save_name` when the save file does not exist.
