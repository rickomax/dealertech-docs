---
layout: default
title: "serialize_field(table, identifier, field_name)"
parent: globals
grand_parent: API Reference
nav_order: 15
---

# serialize_field(table, identifier, field_name)

Registers a field on a Lua table for automatic save/load serialization.

When the game state is saved, all registered fields are written to the save file. When the state is loaded, the saved values are restored into their tables automatically. Supported value types are booleans, numbers, strings, and entity references.

**Parameters**
- `table` (`table`) — The Lua table containing the field to serialize.
- `identifier` (`string`) — A unique identifier used to group serialized fields (typically the entity's class name or instance key).
- `field_name` (`string`) — The key within `table` whose value should be serialized.

**Example**

```lua
function monster.create(class, self_entity)
    local self = {}
    self.health = 100
    self.state = "idle"

    serialize_field(self, self_entity:get_instance_id(), "health")
    serialize_field(self, self_entity:get_instance_id(), "state")

    return self
end
```
