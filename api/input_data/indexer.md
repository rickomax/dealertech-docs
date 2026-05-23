---
layout: default
title: "input_data[index] : number"
parent: input_data
grand_parent: API Reference
nav_order: 1
---

# `input_data[index]` : `number`

Gets or sets the raw float input value at the given index.

**Parameters**
- `index` (`integer`) — The 0-based index of the input slot to access.

---

## Conventions

The exact meaning of each slot is decided by your `read_input` implementation. A common layout is:

| Index | Meaning              |
|-------|----------------------|
| 0     | Move forward (–back) |
| 1     | Strafe right (–left) |
| 2     | Yaw delta            |
| 3     | Pitch delta          |
| 4     | Jump (held)          |
| 5     | Fire (held)          |
| ...   | game-specific        |

