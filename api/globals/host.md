---
layout: default
title: "host()"
parent: globals
grand_parent: API Reference
nav_order: 7
---

# host()

Starts the game as a listen server (host).

Sets the `is_server` and `is_connected` environment flags to `true`, then executes `autoexec.lua`.

**Errors**
- Throws if the network host fails to start.
