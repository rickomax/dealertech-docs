---
layout: default
title: ui_panel
parent: API Reference
---

# `ui_panel`

Exposes a container UI panel to Lua. Panels can host other UI elements and optionally scroll their content when created with `scrollable = true`.

**C# type:** `LuaUIPanel`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaUIPanel.cs`

## Members

### `create`

Creates a new UI panel, optionally parented to another panel and optionally scrollable.

`public static LuaUIPanel Create(LuaUIPanel parent = null, bool scrollable = false)`
