---
layout: default
title: "entity:set_bounciness(bounciness)"
parent: entity
grand_parent: API Reference
nav_order: 62
---

# `entity:set_bounciness(bounciness)`

Configures the entity collision response.

**Parameters**
- `bounciness` (`number`) — `1.0` produces no bounce (the entity slides along surfaces); higher values bounce more, with `2.0` being a fully elastic bounce.

**Notes**
- Has no effect unless the entity move type is `move_type.physics`.
