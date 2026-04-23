---
title: solid
parent: API Reference
---

# `solid`

Provides integer constants that identify the solid/collision types used by `entity.set_solid`.

**C# type:** `LuaSolid`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaSolid.cs`

## Members

### `none`

The entity is non-solid and does not interact with the collision system.

`public int Not`

### `trigger`

The entity reports touch events but does not block movement.

`public int Trigger`

### `bbox`

The entity collides as an axis-aligned bounding box.

`public int BBox`

### `slidebox`

The entity collides as a bounding box and slides along contact surfaces.

`public int SlideBox`

### `bsp`

The entity collides using BSP brush geometry.

`public int BSP`
