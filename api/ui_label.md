---
title: ui_label
parent: API Reference
---

# `ui_label`

Exposes a TextMeshPro text label UI element to Lua. Created as a child of a `ui_panel` via `ui_label.create(panel)`.

**C# type:** `LuaUILabel`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaUILabel.cs`

## Members

### `create`

Creates a new label element and parents it under the given panel.

`public static LuaUILabel Create(LuaUIPanel panel)`

### `set_font`

Sets the font used to render the label's text.

`public void SetFont(LuaFont font)`

### `set_size`

Sets the font size, in points, used to render the label's text.

`public void SetSize(float size)`

### `set_color`

Sets the color of the label's text (RGBA in the range [0, 1]).

`public void SetColor(LuaVector4 color)`

### `set_text`

Sets the text string displayed by the label.

`public void SetText(string text)`
