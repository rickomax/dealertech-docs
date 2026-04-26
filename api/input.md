# `input`

`input` provides Lua-exposed access to the engine input system.

All functions are static and accessed directly from the `input` table.

If a control or action is not found, the functions return a neutral value (`0`).

---

## Binding

### `input.bind(path, code)`
Binds a Lua code string to an input action path. The code is evaluated every time the action is performed.

**Parameters**
- `path` (`string`) — The binding path to listen on (e.g. `<Keyboard>/space`).
- `code` (`string`) — The Lua code string to evaluate when the action fires.

---

## Raw control polling

These functions read directly from raw device control paths (e.g. `<Keyboard>/space`, `<Mouse>/delta/x`, `<Gamepad>/leftStick/x`).

### `input.read_raw_float(path) -> number`
Reads the current float value of a raw control.

**Parameters**
- `path` (`string`) — Raw control path.

**Returns**
- `number` — Current float value, or `0` if the control is not found or is not a float control.

---

### `input.is_held(path) -> number`
Returns whether a raw control is currently being held down.

**Parameters**
- `path` (`string`) — Raw control path (e.g. `<Keyboard>/space`).

**Returns**
- `number` — `1` if held, `0` otherwise.

---

### `input.was_pressed(path) -> number`
Returns `1` the first time a raw control transitions from inactive to active.

The previous value is tracked internally per `path`, so this should be polled once per frame.

**Parameters**
- `path` (`string`) — Raw control path.

**Returns**
- `number` — `1` on the press transition, `0` otherwise.

---

## Deprecated

The following functions read from named input actions defined in the engine's input asset. They are deprecated in favor of the raw-control functions above.

### `input.read_vector(actionPath) -> vector`  *(deprecated)*
Reads a 2D input action and returns it as a 3D vector with `z = 0`. Returns a zero vector if the action is not found.

### `input.read_input_down(actionPath) -> number`  *(deprecated)*
Returns `1` if the action was pressed during the current frame, `0` otherwise.

### `input.read_input_pressed(actionPath) -> number`  *(deprecated)*
Returns `1` while the action is currently held down, `0` otherwise.

---

## Example

```lua
input.bind("<Keyboard>/escape", "show_menu()")

local mouseX = input.read_raw_float("<Mouse>/delta/x")

if input.is_held("<Keyboard>/w") == 1 then
    -- moving forward
end

if input.was_pressed("<Keyboard>/space") == 1 then
    -- jump pressed this frame
end
```
