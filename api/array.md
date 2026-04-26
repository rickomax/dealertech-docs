---
layout: default
title: array
parent: API Reference
---

# `array`

`array` is a dynamic, 1-indexed container exposed to Lua.
It stores arbitrary values and supports the `#` length operator.

Most engine APIs that return a list of entities (such as `physics.get_entities_in_radius`) return an `array`.

---

## Creation

### `array.create(capacity) -> array`
Creates a new empty array with the given initial capacity hint.

**Parameters**
- `capacity` (`integer`, default `1`) — Initial capacity hint.

**Returns**
- `array`

You can also call the namespace directly:

```lua
local a = array(8)
```

---

## Functions

### `array:add(value)`
Appends a value to the end of the array.

**Parameters**
- `value` (`any`) — The value to append.

---

### `array:get(index) -> any`
Returns the value at a 1-based index.

**Parameters**
- `index` (`integer`) — The 1-based index of the element to retrieve.

**Returns**
- `any` — The value stored at `index`.

---

### `array:remove_at(index)`
Removes the element at a 1-based index.

**Parameters**
- `index` (`integer`) — The 1-based index of the element to remove.

---

### `array:clear()`
Removes all elements from the array.

---

## Operators

### Length

`#a` returns the number of elements in the array.

---

## Example

```lua
local items = array.create(4)
items:add("sword")
items:add("shield")

for i = 1, #items do
    print(items:get(i))
end

items:remove_at(1)
items:clear()
```
