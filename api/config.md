---
layout: default
title: config
parent: API Reference
has_children: true
nav_order: 3
---

# `config`

`config` provides persistent key/value configuration storage exposed to Lua.

Values are stored as named numbers or strings and survive between sessions.

All functions are static and accessed directly from the `config` table.
