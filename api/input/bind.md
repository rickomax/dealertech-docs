---
layout: default
title: "`input.bind(path, code)`"
parent: input
grand_parent: API Reference
nav_order: 1
---

# `input.bind(path, code)`

Binds a Lua code string to an input action path. The code is evaluated every time the action is performed.

**Parameters**
- `path` (`string`) — The binding path to listen on (e.g. `<Keyboard>/space`).
- `code` (`string`) — The Lua code string to evaluate when the action fires.

---

## Raw control polling

These functions read directly from raw device control paths (e.g. `<Keyboard>/space`, `<Mouse>/delta/x`, `<Gamepad>/leftStick/x`).
