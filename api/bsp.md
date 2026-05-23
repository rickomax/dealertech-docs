---
layout: default
title: bsp
parent: API Reference
has_children: true
nav_order: 2
---

# `bsp`

`bsp` provides Lua-exposed BSP map utilities and contents queries based on the currently loaded BSP data.

It can be used to enumerate available maps, query *contents* at a point, and classify a line segment against the BSP.

> Notes:
> - `point_contents` and `trace_contents` depend on BSP clip/leaf/plane data being available (typically after loading a BSP).
> - Contents values are returned as integers (the same numeric IDs used by the engine for contents types).
