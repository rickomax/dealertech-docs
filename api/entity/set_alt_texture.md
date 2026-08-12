---
layout: default
title: "entity:set_alt_texture(value)"
parent: entity
grand_parent: API Reference
nav_order: 74
---

# `entity:set_alt_texture(value)`

Switches the entity BSP model between its regular and alternate texture animations.

Quake textures whose name starts with `+` and a digit (`+0butn`, `+1butn`, ...) form one animation, and the same name with a letter (`+abutn`, `+bbutn`, ...) forms a second, alternate one. Both are baked into the map when it loads, so switching between them costs nothing at runtime. This is how buttons, switches and similar brush entities show an "on" and an "off" face.

**Parameters**
- `value` (`boolean`) — `true` to render the alternate animation, `false` to render the regular one.

**Notes**
- Has no effect when not running on the server.
- Has no effect when the entity has no BSP model, or when none of the model's textures declare alternate frames.
- Applies to both map submodels (`entity:set_model("*3")`) and standalone `.bsp` entity models.
- The value is replicated to clients, so all of them see the same animation.

**Example**
```lua
function button:use()
    self:set_alt_texture(not self:get_alt_texture())
end
```
