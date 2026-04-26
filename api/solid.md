# `solid`

`solid` exposes the solid type constants used with `entity:set_solid`.

All members are integer constants accessed directly from the `solid` table.

---

## Constants

### `solid.none` : `integer`
The entity has no collision.

### `solid.trigger` : `integer`
The entity is a non-blocking trigger volume.

### `solid.bbox` : `integer`
The entity uses an axis-aligned bounding box for collision.

### `solid.slidebox` : `integer`
The entity uses a sliding axis-aligned bounding box for collision.

### `solid.bsp` : `integer`
The entity uses BSP brush collision.

---

## Example

```lua
self:set_solid(solid.bbox)
self:set_size(vector.create(-16, -16, -24), vector.create(16, 16, 32))

-- Trigger volume
trigger_ent:set_solid(solid.trigger)
```
