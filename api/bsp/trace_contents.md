---
layout: default
title: "`bsp.trace_contents(start, end, result)`"
parent: bsp
grand_parent: API Reference
nav_order: 3
---

# `bsp.trace_contents(start, end, result)`

Classifies a segment from `start` to `end` against the BSP and writes the contents flags into `result`.

This function does **not** return a value; it updates the provided `result` object in place.

**Parameters**
- `start` (`vector`) — Segment start position.
- `end` (`vector`) — Segment end position.
- `result` (`trace_result`) — Output object that receives the contents classification.
