---
layout: default
title: physics
parent: API Reference
has_children: true
nav_order: 17
---

# `physics`

`physics` provides Lua-exposed physics queries and trace operations.

The trace functions return a `trace_result` object describing the first hit (if any), including impact normal, end position, traveled distance and the hit entity's instance table.

The overlap functions return a 1-indexed Lua `table` of entity instance tables found inside a volume.
