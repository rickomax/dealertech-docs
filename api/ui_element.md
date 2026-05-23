---
layout: default
title: ui_element
parent: API Reference
has_children: true
nav_order: 24
---

# `ui_element`

`ui_element` is the base class shared by all UI elements exposed to Lua.

The following types inherit these members:
- `ui_panel`
- `ui_label`
- `ui_image`
- `ui_input_field`

You don't construct `ui_element` directly — call `create` on a derived type instead.
