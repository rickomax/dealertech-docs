---
layout: default
title: "ui_input_field:set_on_submit(callback)"
parent: ui_input_field
grand_parent: API Reference
nav_order: 11
---

# `ui_input_field:set_on_submit(callback)`

Registers a callback invoked when the user submits the input (e.g. presses Enter).

Replaces any previously registered change listener.

**Parameters**
- `callback` (`function`) — Lua function invoked with the submitted text value as its argument.
