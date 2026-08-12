---
layout: default
title: "entity:play_sound(filename, channel, volume, attenuation)"
parent: entity
grand_parent: API Reference
nav_order: 61
---

# `entity:play_sound(filename, channel, volume, attenuation)`

Plays a sound at the entity position.

**Parameters**
- `filename` (`string`) — Sound filename.
- `channel` (`integer`) — Audio channel, from [`sound_channel`](../sound_channel.html).
- `volume` (`number`) — Volume in `[0, 1]`.
- `attenuation` (`number`) — Distance falloff, from [`sound_atten`](../sound_atten.html).

`sound_atten.none` disables 3D positioning, so the sound appears to come from the listener
wherever the emitter is. Use `sound_atten.normal` for anything a player should be able to locate.

**Server-only**

