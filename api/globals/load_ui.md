---
layout: default
title: "load_ui(filename, parent)"
parent: globals
grand_parent: API Reference
nav_order: 19
---

# load_ui(filename, parent)

Loads a UI definition file from the `ui` folder and returns its root element.

**Parameters**
- `filename` (`string`) — The UI definition filename.
- `parent` (`ui_element`, optional) — An existing element to parent the loaded UI to.

**Returns**
- (`ui_element`) — The root element of the loaded UI.

Throws `ui_transpiler_parse_error` when the file cannot be parsed, or a file-not-found error when it does not exist.
