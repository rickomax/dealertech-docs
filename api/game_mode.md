---
layout: default
title: game_mode
parent: API Reference
has_children: true
nav_order: 32
---

# `game_mode`

`game_mode` represents a game mode definition. Several may exist at once; exactly one is
current, and the current one sets the game name and type.

A mode is backed by a Lua class, the same way an entity is. The class must be a global table
named as passed to `game_mode.create`, and must define a `create` function returning an
instance table:

```lua
deathmatch = {}

function deathmatch.load_resources()          -- optional
end

function deathmatch:create(native)            -- required, must return a table
    native:set_name("Deathmatch")
    native:set_type("deathmatch")
    native:set_max_players(8)
    return make_instance(self, native)
end

function deathmatch:has_skills() return false end   -- optional
function deathmatch:enable() end                    -- optional
function deathmatch:disable() end                   -- optional
function deathmatch:update() end                    -- optional
```

Creating one and making it current:

```lua
local mode = game_mode.create("deathmatch")
mode.native:set_current(true)
```

`create` returns the *instance table*, so the native object is `mode.native`. `get_current`
returns the native directly.

Modes also carry the same networked variables as `entity`, for mode state such as scores and
round timers that client scripts need to read. They behave identically here:
[`get_net_number`](../entity/get_net_number.html),
[`set_net_number`](../entity/set_net_number.html),
[`get_net_string`](../entity/get_net_string.html),
[`set_net_string`](../entity/set_net_string.html),
[`get_net_vector`](../entity/get_net_vector.html),
[`set_net_vector`](../entity/set_net_vector.html),
[`get_net_table`](../entity/get_net_table.html) and
[`set_net_table`](../entity/set_net_table.html).

**Optional Lua callbacks**

| Function | Called |
|:---------|:-------|
| `load_resources()` | Before `create`, on the server and on clients. |
| `create(native)` | Once, on the server, when the mode is spawned. |
| `has_skills()` | Whenever something asks whether the mode is played at a skill level. |
| `enable()` | On the server, when the mode becomes current. |
| `disable()` | On the server, when the mode stops being current. |
| `update()` | Every physics tick on the server, while the mode is current. |

Creating a mode requires the server to be running, and setter functions only have an effect
on the server. Configuration is locked once the mode becomes current.
