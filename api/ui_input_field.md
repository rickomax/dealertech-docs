---
title: ui_input_field
parent: API Reference
---

# `ui_input_field`

Lua API object exposed as <c>ui_input_field</c>.

**C# type:** `LuaUIInputField`  

**Source:** `Assets/DealerTech/Runtime/Lua/LuaUIInputField.cs`

## Members

### `create`

Lua member <c>create</c>.

`public static LuaUIInputField Create(LuaUIPanel panel)`

### `set_font`

Lua member <c>set_font</c>.

`public void SetFont(LuaFont font)`

### `set_size`

Lua member <c>set_size</c>.

`public void SetSize(float size)`

### `set_color`

Lua member <c>set_color</c>.

`public void SetColor(LuaVector4 color)`

### `set_text`

Lua member <c>set_text</c>.

`public void SetText(string text)`

### `get_text`

Lua member <c>get_text</c>.

`public string GetText()`

### `set_content_type`

Lua member <c>set_content_type</c>.

`public void SetContentType(string contentType)`

### `set_char_limit`

Lua member <c>set_char_limit</c>.

`public void SetCharacterLimit(int limit)`

### `on_change`

Lua member <c>on_change</c>.

`public void OnChange(LuaFunction callback)`

### `on_submit`

Lua member <c>on_submit</c>.

`public void OnSubmit(LuaFunction callback)`
