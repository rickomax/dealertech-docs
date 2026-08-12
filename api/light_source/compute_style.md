---
layout: default
title: "light_source.compute_style(style)"
parent: light_source
grand_parent: API Reference
nav_order: 5
---

# `light_source.compute_style(style)`

Registers a light style animation string and returns its index.

**Parameters**
- `style` (`string`) - one character per frame, from `a` (black) to `z` (brightest)

**Returns**
- `number` - the 1-based style index, or `0` when not running on the server
