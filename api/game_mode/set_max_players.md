---
layout: default
title: "game_mode:set_max_players(value)"
parent: game_mode
grand_parent: API Reference
nav_order: 12
---

# `game_mode:set_max_players(value)`

Sets how many players this mode accepts. While the mode is current, clients connecting
beyond this count are refused.

**Parameters**
- `value` (`number`) - the maximum player count, counting the host

**Server-only**, and ignored once the mode is current.
