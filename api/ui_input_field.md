---
layout: default
title: ui_input_field
parent: API Reference
---

# `ui_input_field`

Exposes a TextMeshPro single-line input field UI element to Lua. Created as a child of a `ui_panel` via `ui_input_field.create(panel)`.

**C# type:** `LuaUIInputField`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaUIInputField.cs`

## Members

### `create`

Creates a new input field element and parents it under the given panel.

`public static LuaUIInputField Create(LuaUIPanel panel)`

### `set_font`

Sets the font used to render the input field's text.

`public void SetFont(LuaFont font)`

### `set_size`

Sets the font size, in points, used to render the input field's text.

`public void SetSize(float size)`

### `set_color`

Sets the color of the input field's text (RGBA in the range [0, 1]).

`public void SetColor(LuaVector4 color)`

### `set_text`

Sets the current text content of the input field.

`public void SetText(string text)`

### `get_text`

Returns the current text content of the input field.

`public string GetText()`

### `set_content_type`

Sets the content validation type of the input field. Supported values are `"integer"`, `"decimal"`, `"password"`, `"email"`; any other value is treated as standard text.

`public void SetContentType(string contentType)`

### `set_char_limit`

Sets the maximum number of characters the field will accept.

`public void SetCharacterLimit(int limit)`

### `on_change`

Installs a Lua callback that fires whenever the field's text value changes. The callback is invoked with the new text string as its single argument.

`public void OnChange(LuaFunction callback)`

### `on_submit`

Installs a Lua callback that fires when the user submits the field (e.g. pressing Enter). The callback is invoked with the submitted text string as its single argument.

`public void OnSubmit(LuaFunction callback)`
