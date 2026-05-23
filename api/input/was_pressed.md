---
layout: default
title: "`input.was_pressed(path) -> number`"
parent: input
grand_parent: API Reference
nav_order: 4
---

# `input.was_pressed(path) -> number`

Returns `1` the first time a raw control transitions from inactive to active.

The previous value is tracked internally per `path`, so this should be polled once per frame.

**Parameters**
- `path` (`string`) — Raw control path.

**Returns**
- `number` — `1` on the press transition, `0` otherwise.

---

## Deprecated

The following functions read from named input actions defined in the engine's input asset. They are deprecated in favor of the raw-control functions above.
