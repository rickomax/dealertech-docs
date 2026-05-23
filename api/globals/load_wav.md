---
layout: default
title: "load_wav(filename)"
parent: globals
grand_parent: API Reference
nav_order: 4
---

# load_wav(filename)

Precaches a sound file so it can be played by entities.

Loads the WAV file into an audio clip and stores it in the resource cache. Subsequent calls with the same filename are ignored.

**Parameters**
- `filename` (`string`) — WAV filename relative to the `sounds` folder (e.g. `"shotgn2.wav"`).

**Errors**
- Throws if the file is not found.
