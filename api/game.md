---
layout: default
title: game
parent: API Reference
---
# `game`

`game` provides Lua access to the global game session state, including the
current skill level and the active game type.

Both values are networked from the server to all clients. The setter functions
only have an effect when called on the server.

---

## Functions

### `game.set_skill(value)`
Sets the current skill level.

**Parameters**
- `value` (`integer`) — The new skill level.

**Server-only**
- Has no effect when not running on the server.

---

### `game.get_skill() -> integer`
Returns the current skill level.

**Returns**
- `integer` — The current skill level.

---

### `game.set_type(value)`
Sets the current game type identifier. The value is stored lower-cased.

**Parameters**
- `value` (`string`) — The game type identifier (for example `"single_player"`).

**Server-only**
- Has no effect when not running on the server.

---

### `game.get_type() -> string`
Returns the current game type identifier.

**Returns**
- `string` — The current game type, lower-cased.
