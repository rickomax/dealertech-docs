---
layout: default
title: sound_channel
parent: API Reference
nav_order: 30
---

# `sound_channel`

`sound_channel` exposes the channel constants used with `entity:play_sound`.

One sound plays per entity per channel; starting a new one on a channel replaces the sound
already playing there.

All members are integer constants accessed directly from the `sound_channel` table.

| Member | Used for |
|:-------|:---------|
| `sound_channel.auto` | Picks the first channel that is free on the entity. |
| `sound_channel.weapon` | Weapon fire. |
| `sound_channel.voice` | Speech and pain sounds. |
| `sound_channel.item` | Item pickups. |
| `sound_channel.body` | Movement and impact sounds. |

**Example**

```lua
self.native:play_sound("weapons/pkup.wav", sound_channel.item, 1, sound_atten.normal)
```
