---
layout: default
title: bsp
parent: API Reference
---
# `bsp`

`bsp` provides Lua-exposed BSP map utilities and contents queries based on the currently loaded BSP data.

It can be used to enumerate available maps, query *contents* at a point, and classify a line segment against the BSP.

> Notes:
> - `point_contents` and `trace_contents` depend on BSP clip/leaf/plane data being available (typically after loading a BSP).
> - Contents values are returned as integers (the same numeric IDs used by the engine for contents types).

---

## Functions

### `bsp.get_maps() -> table`
Returns a 1-indexed table of every BSP map name (without extension) available in the engine's `maps` folder.

**Returns**
- `table` — `{ [1] = "e1m1", [2] = "e1m2", ... }`

---

### `bsp.point_contents(pos) -> integer`
Returns the contents value of the BSP leaf containing the given point.

**Parameters**
- `pos` (`vector`) — Point to test.

**Returns**
- `integer` — Contents id at that point.

---

### `bsp.trace_contents(start, end, result)`
Classifies a segment from `start` to `end` against the BSP and writes the contents flags into `result`.

This function does **not** return a value; it updates the provided `result` object in place.

**Parameters**
- `start` (`vector`) — Segment start position.
- `end` (`vector`) — Segment end position.
- `result` (`trace_result`) — Output object that receives the contents classification.
