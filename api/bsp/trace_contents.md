---
layout: default
title: "bsp.trace_contents(start, end, result) -> integer"
parent: bsp
grand_parent: API Reference
nav_order: 3
---

# `bsp.trace_contents(start, end, result) -> integer`

Classifies a segment from `start` to `end` against the BSP, splitting it at every plane
crossing. If the segment runs into solid space, `result` is filled in with the impact
fraction/position/normal at the boundary where it entered solid, the same way a physics
trace would. Otherwise `result.fraction` is `1` and `result.end_position` is `end`.

This function does **not** return a value directly; it updates the provided `result`
object in place and returns the contents classification instead.

**Parameters**
- `start` (`vector`) — Segment start position.
- `end` (`vector`) — Segment end position.
- `result` (`trace_result`) — Output object that receives the trace data.

**Returns**
- `integer` — Contents id at the impact or end position.

