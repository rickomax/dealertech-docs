---
layout: default
title: entity
parent: API Reference
has_children: true
nav_order: 4
---

# `entity`

`entity` represents a game entity instance and its Lua-exposed properties, movement, state and networked variables.

It exposes helpers for:
- Reading/writing string properties
- Finding other entities
- Querying and changing transform / movement data
- Managing simple state-machine state (`entity_state`)
- Reading/writing networked numbers, strings and vectors
- Spawning, despawning and teleporting entities
- Basic line-of-sight client checks
- Playing sounds

Most setter functions only have an effect when called on the server (they will do nothing when called on a non-server instance).
