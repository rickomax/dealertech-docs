---
title: light
parent: API Reference
---

# `light`

Represents a networked point light attached to the world or to a parent entity. Exposed to Lua as `light`; instances are created from Lua through `lights.create_light`.

**C# type:** `GameLight`  

**Source:** `Assets/DealerTech/Runtime/Entities/GameLight.cs`

## Members

### `set_intensity`

Sets the intensity of this light. Only runs on the server.

`public void SetIntensity(float value)`
