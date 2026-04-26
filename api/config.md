---
layout: default
title: config
parent: API Reference
---
# `config`

`config` provides persistent key/value configuration storage exposed to Lua.

Values are stored as named numbers or strings and survive between sessions.

All functions are static and accessed directly from the `config` table.

---

## Functions

### `config.load()`
Loads the configuration values from disk into memory.

---

### `config.save()`
Saves the in-memory configuration values to disk.

---

### `config.get_number(key) -> number`
Returns the stored numeric value for the given key.

**Parameters**
- `key` (`string`) — The configuration key.

**Returns**
- `number` — The stored value, or `0` if the key does not exist.

---

### `config.set_number(key, value)`
Sets the numeric value for the given key.

**Parameters**
- `key` (`string`) — The configuration key.
- `value` (`number`) — The new value.

---

### `config.get_string(key) -> string`
Returns the stored string value for the given key.

**Parameters**
- `key` (`string`) — The configuration key.

**Returns**
- `string|nil` — The stored value, or `nil` if the key does not exist.

---

### `config.set_string(key, value)`
Sets the string value for the given key.

**Parameters**
- `key` (`string`) — The configuration key.
- `value` (`string`) — The new value.
