---
layout: default
title: move_type
parent: API Reference
---

# `move_type`

Provides integer constants that identify the movement types used by `entity.set_move_type`.

**C# type:** `LuaMoveType`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaMoveType.cs`

## Members

### `none`

The entity is not moved by the physics simulation.

`public int None`

### `walk`

The entity walks on the ground using character controller movement.

`public int Walk`

### `step`

The entity steps along the ground, snapping to surfaces.

`public int Step`

### `fly`

The entity flies, ignoring gravity.

`public int Fly`

### `toss`

The entity is tossed and affected by gravity, stopping on collision.

`public int Toss`

### `flymissile`

The entity flies as a missile, ignoring gravity and stopping on collision.

`public int FlyMissile`

### `bounce`

The entity bounces off surfaces it collides with.

`public int Bounce`

### `push`

The entity is push-driven, moving other entities out of the way.

`public int Push`

### `noclip`

The entity moves freely and ignores world collision.

`public int NoClip`
