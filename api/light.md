---
layout: default
title: light
parent: API Reference
---

# `light`

`light` represents a networked dynamic light spawned via `lights.create_light`.

Each light synchronizes its position, colour, intensity and radius across clients.

Lights are usually created through the `lights.create_light` factory rather than constructed directly.

---

## Functions

### `light:set_intensity(value)`
Sets the light intensity.

**Parameters**
- `value` (`number`) — The new intensity value.

**Server-only**
- Has no effect when not running on the server.

---

## Example

```lua
local torch = lights.create_light(
    self:get_origin(),
    vector.create(1.0, 0.7, 0.3),
    2.0,                      -- intensity
    256.0,                    -- radius
    false,                    -- isStatic
    self                      -- parent entity
)

-- Later, dim it down
torch:set_intensity(0.5)
```
