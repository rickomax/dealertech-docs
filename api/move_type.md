# `move_type`

`move_type` exposes the movement type constants used with `entity:set_move_type`.

All members are integer constants accessed directly from the `move_type` table.

---

## Constants

### `move_type.none` : `integer`
No movement processing applied.

### `move_type.walk` : `integer`
Walking movement with ground friction.

### `move_type.step` : `integer`
Stepped movement used by NPCs that snap to the ground.

### `move_type.fly` : `integer`
Free-flight movement with no gravity.

### `move_type.toss` : `integer`
Tossed projectile movement affected by gravity.

### `move_type.flymissile` : `integer`
Flying projectile movement that ignores gravity.

### `move_type.bounce` : `integer`
Bouncing movement that reflects off surfaces.

### `move_type.push` : `integer`
Pushed movement, used by movers such as doors and platforms.

### `move_type.noclip` : `integer`
Free movement that ignores all collisions.

---

## Example

```lua
-- Make this entity a tossed projectile
self:set_move_type(move_type.toss)

-- Make a door
self:set_move_type(move_type.push)
```
