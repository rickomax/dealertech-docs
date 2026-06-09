---
layout: default
title: "ui_element:add_binding(getter, setter)"
parent: ui_element
grand_parent: API Reference
nav_order: 8
---

# `ui_element:add_binding(getter, setter)`

Adds a reactive binding to this element. Each tick the `getter` is evaluated and, when its result changes, the `setter` is called with that result. The binding is removed automatically when the element is destroyed.

**Parameters**
- `getter` (`function`) — Returns the current value(s).
- `setter` (`function`) — Applies the value(s) returned by the getter.

**Example**

```lua
label:add_binding(
    function() return get_score() end,
    function(value) label:set_text(value) end)
```

In ASP markup, the `<%=# expr %>` syntax compiles to an `add_binding` call. See the [ASP Template Format](../../asp.html) guide.
