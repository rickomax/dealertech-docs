---
layout: default
title: sound_atten
parent: API Reference
nav_order: 31
---

# `sound_atten`

`sound_atten` exposes the attenuation constants used with `entity:play_sound`.

The value scales how quickly a sound fades with distance; higher attenuates faster.

All members are integer constants accessed directly from the `sound_atten` table.

| Member | Falloff |
|:-------|:--------|
| `sound_atten.none` | None. The sound plays at full volume anywhere on the map, in 2D. |
| `sound_atten.normal` | Standard, for gameplay sounds such as weapons and footsteps. |
| `sound_atten.idle` | Faster, for idle and ambient loops that should stay local. |
| `sound_atten.static` | Fastest, for static emitters audible only up close. |

`sound_atten.none` is not a "default" — it disables 3D positioning entirely, so the sound
appears to come from the listener wherever the emitter is. Use `sound_atten.normal` for
anything a player should be able to locate.

**Example**

```lua
self.native:play_sound("player/plyrjmp8.wav", sound_channel.body, 1, sound_atten.normal)
```
