---
layout: default
title: trace_result
parent: API Reference
---

# `trace_result`

`trace_result` represents the output of a physics trace operation.

It contains collision information and surface data for the first hit.

Instances are typically returned by:
- `physics.trace_line`
- `physics.trace_hull`

---

## Fields

### `start_solid` : `boolean`
`true` if the starting point of the trace was inside a blocking volume.

---

### `fraction` : `number`
Normalized distance traveled before impact, in the range `[0, 1]`.

- `1.0` → No hit (reached full distance)
- `< 1.0` → Hit occurred before reaching the end

---

### `end_position` : `vector`
Final position of the trace.

- If no collision occurred, this equals the trace end.
- If a collision occurred, this is the impact point.

---

### `normal` : `vector`
Surface normal at the impact point.

Zero vector if no collision occurred.

---

### `distance` : `number`
World distance traveled before impact.

---

### `hit_table` : `table|nil`
Lua instance table of the entity that was hit, or `nil` if nothing was hit or the hit collider does not belong to an entity.

---

## Creation

Trace results are created internally by the engine.

```lua
local tr = physics.trace_line(...)
```

---

## Typical Usage

```lua
local tr = physics.trace_line(
    self:get_origin(),
    self:get_origin() + forward * 2048,
    0,        -- collisionType
    self,     -- ignore
    false     -- debug
)

if tr.fraction < 1 then
    print("Hit at:", tostring(tr.end_position))
    print("Distance:", tr.distance)
    if tr.hit_table ~= nil then
        print("Hit entity:", tr.hit_table)
    end
end

if tr.start_solid then
    print("Started inside solid")
end
```
