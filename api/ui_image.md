---
layout: default
title: ui_image
parent: API Reference
---

# `ui_image`

Exposes a raw image UI element to Lua. Created as a child of a `ui_panel` via `ui_image.create(panel)`.

**C# type:** `LuaUIImage`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaUIImage.cs`

## Members

### `create`

Creates a new image element and parents it under the given panel.

`public static LuaUIImage Create(LuaUIPanel panel)`

### `set_image`

Sets the texture displayed by the image.

`public void SetImage(string filename)`

### `set_size`

Sets the explicit size of the image in pixels.

`public void SetSize(float width, float height)`

### `set_color`

Sets the tint color of the image (RGBA in the range [0, 1]).

`public void SetColor(LuaVector4 color)`

### `set_native_size`

Resizes the image to match the native pixel dimensions of its texture.

`public void SetNativeSize()`
