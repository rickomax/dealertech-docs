---
layout: default
title: light_source
parent: API Reference
has_children: true
nav_order: 11
---

# `light_source`

`light_source` represents a networked dynamic light spawned at runtime, and also
provides BSP light style helpers used by maps with animated lights.

Each light instance synchronizes its position, colour, intensity and radius
across clients. Lights are created through `light_source.create` rather than
constructed directly.

Most static functions are server-authoritative — calling them on a non-server
instance has no effect.
