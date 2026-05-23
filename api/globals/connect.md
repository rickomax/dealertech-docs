---
layout: default
title: "connect(address, port)"
parent: globals
grand_parent: API Reference
nav_order: 8
---

# connect(address, port)

Connects to a remote game server as a client.

Configures the network transport, sets `is_server` to `false` and `is_connected` to `true`, then executes `autoexec.lua`.

**Parameters**
- `address` (`string`) — Server IP address or hostname.
- `port` (`integer`, default `7777`) — Server port number.

**Errors**
- Throws if the connection fails to start.
