---
layout: default
title: contents
parent: API Reference
nav_order: 29
---

# `contents`

`contents` exposes the BSP leaf content constants returned by `bsp.point_contents`.

All members are integer constants accessed directly from the `contents` table.

| Member | Meaning |
|:-------|:--------|
| `contents.empty` | Open air. |
| `contents.solid` | Solid world geometry. |
| `contents.water` | Water volume. |
| `contents.slime` | Slime volume. |
| `contents.lava` | Lava volume. |
| `contents.sky` | Sky surface. |
| `contents.origin` | Brush origin marker, stripped when the map is compiled. |
| `contents.clip` | Clip brush, solid to entities but not rendered. |
| `contents.current0` | Current-carrying volume that pushes entities along it. |

**Example**

```lua
local where = bsp.point_contents(self.native:get_origin())
if where == contents.lava then
    inflict_damage(self, nil, nil, 20)
end
```
