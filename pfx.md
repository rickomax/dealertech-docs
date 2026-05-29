---
layout: default
title: PFX File Format
nav_order: 4
---

# PFX File Format

PFX is the stack-based assembly language used to program particle effects and fullscreen screen effects.

A PFX file is loaded with `load_pfx` and played via `particles.spawn` (world-space particles) or `screen.play_effect` (fullscreen post-process). The same instruction set runs on the CPU (Burst-compiled particle jobs) and on the GPU (HLSL fragment shader for screen effects).

## File Structure

A PFX file has two optional sections, `start:` and `update:`.

```
start:
<instructions executed once when each particle spawns>

update:
<instructions executed every frame for each particle>
```

- **`start:`** — Runs once per particle at spawn time. Use it to set initial position, velocity, color and size. Screen effects ignore this section.
- **`update:`** — Runs every frame (particles) or every pixel per frame (screen effects). Use it to move particles, fade alpha, sample textures, etc.

Blank lines are ignored. Comments begin with `//`, `;`, or `#` and extend to the end of the line. Instructions are case-insensitive. Multiple instructions can appear on the same line separated by whitespace.

## Execution Model

The VM uses a **float stack** (128 slots for particles, 64 for screen effects). Most instructions push or pop values. There are no named variables; you read a register with a `GET_*` instruction (pushes a value) and write it back with a `SET_*` instruction (pops a value).

Arithmetic operations pop their operands and push the result. For binary operations, the **first** pushed value is the left-hand operand (i.e. `A B SUB` computes `A - B`).

## Instructions

### Constants

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `CONST <value>` | — → value | Push a literal float. The value follows the mnemonic on the same line. |

### Emitter Registers

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_EX` | — → float | Emitter X position (particle) or pixel U coordinate (screen). |
| `GET_EY` | — → float | Emitter Y position (particle) or pixel V coordinate (screen). |
| `GET_EZ` | — → float | Emitter Z position (particle only; 0 for screen). |
| `GET_DX` | — → float | Emitter direction X (particle only; 0 for screen). |
| `GET_DY` | — → float | Emitter direction Y (particle only; 0 for screen). |
| `GET_DZ` | — → float | Emitter direction Z (particle only; 0 for screen). |

### Particle Position

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_PX` | — → float | Current particle X position. |
| `GET_PY` | — → float | Current particle Y position. |
| `GET_PZ` | — → float | Current particle Z position. |
| `SET_PX` | float → — | Set particle X position. |
| `SET_PY` | float → — | Set particle Y position. |
| `SET_PZ` | float → — | Set particle Z position. |

### Particle Velocity

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_VX` | — → float | Current particle X velocity. |
| `GET_VY` | — → float | Current particle Y velocity. |
| `GET_VZ` | — → float | Current particle Z velocity. |
| `SET_VX` | float → — | Set particle X velocity. |
| `SET_VY` | float → — | Set particle Y velocity. |
| `SET_VZ` | float → — | Set particle Z velocity. |

### Particle Size

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_PS` | — → float | Current particle size. |
| `SET_PS` | float → — | Set particle size. |

### Particle Color (RGBA)

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_PR` | — → float | Red channel (0–1). For screen effects, reads the current pixel red. |
| `GET_PG` | — → float | Green channel. |
| `GET_PB` | — → float | Blue channel. |
| `GET_PA` | — → float | Alpha channel. |
| `SET_PR` | float → — | Set red channel. For screen effects, writes to the output pixel red. |
| `SET_PG` | float → — | Set green channel. |
| `SET_PB` | float → — | Set blue channel. |
| `SET_PA` | float → — | Set alpha channel. |

### Metadata

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_INDEX` | — → float | Index of the current particle in the batch (0 for screen). |
| `GET_COUNT` | — → float | Total number of particles in the effect (0 for screen). |
| `GET_TIME` | — → float | Global elapsed time in seconds. |
| `GET_DT` | — → float | Frame delta time in seconds. |
| `GET_AGE` | — → float | Time elapsed since the particle spawned (particle) or since the effect started (screen). |
| `GET_LIFE` | — → float | Total lifetime of the particle (particle) or effect duration (screen). |
| `GET_RND` | — → float | Push a pseudo-random value in 0–1. Deterministic per particle/pixel and frame. |

### Arithmetic

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `ADD` | a b → (a + b) | Addition. |
| `SUB` | a b → (a - b) | Subtraction. |
| `MUL` | a b → (a * b) | Multiplication. |
| `DIV` | a b → (a / b) | Division. Returns 0 when the divisor is near zero. |
| `NEG` | a → (-a) | Negate top of stack. |
| `SIN` | a → sin(a) | Sine (radians). |
| `COS` | a → cos(a) | Cosine (radians). |
| `ABS` | a → \|a\| | Absolute value. |
| `SQRT` | a → sqrt(a) | Square root (negative inputs clamped to 0). |
| `MIN` | a b → min(a, b) | Minimum of two values. |
| `MAX` | a b → max(a, b) | Maximum of two values. |
| `STEP` | edge x → 0 or 1 | Returns 1 if x >= edge, otherwise 0. |

### Texture Sampling (screen effects)

These instructions are only meaningful in screen effects. In particle mode, getters return 0 and setters are no-ops.

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_TX` | — → float | Texel width (1 / texture width). |
| `GET_TY` | — → float | Texel height (1 / texture height). |
| `SET_SX` | float → — | Set the sample U coordinate. |
| `SET_SY` | float → — | Set the sample V coordinate. |
| `SAMPLE` | — → — | Sample the screen texture at (SX, SY). Stores the result internally. |
| `GET_SR` | — → float | Red channel of the last `SAMPLE` result. |
| `GET_SG` | — → float | Green channel of the last `SAMPLE` result. |
| `GET_SB` | — → float | Blue channel of the last `SAMPLE` result. |
| `GET_SA` | — → float | Alpha channel of the last `SAMPLE` result. |

### External Registers (screen effects)

These read from float and color buffers passed by Lua. In particle mode they return 0.

| Mnemonic | Stack Effect | Description |
|:---------|:-------------|:------------|
| `GET_FLOAT` | index → float | Pop an index, push the float at that index from the external float buffer. |
| `GET_COLOR` | index → — | Pop an index, load the color at that index into the color register. |
| `GET_CR` | — → float | Red channel of the color register. |
| `GET_CG` | — → float | Green channel of the color register. |
| `GET_CB` | — → float | Blue channel of the color register. |
| `GET_CA` | — → float | Alpha channel of the color register. |

## Examples

### Explosion (particle effect)

```
start:
GET_EX GET_RND CONST 32 MUL CONST 16 SUB ADD SET_PX
GET_EY GET_RND CONST 32 MUL CONST 16 SUB ADD SET_PY
GET_EZ GET_RND CONST 32 MUL CONST 16 SUB ADD SET_PZ

GET_RND CONST 2 MUL CONST 1 SUB CONST 100 MUL SET_VX
GET_RND CONST 2 MUL CONST 1 SUB CONST 100 MUL SET_VY
GET_RND CONST 2 MUL CONST 1 SUB CONST 100 MUL SET_VZ

CONST 6 SET_PS
CONST 1 SET_PA

update:
GET_PX GET_VX GET_DT MUL ADD SET_PX
GET_PY GET_VY GET_DT MUL ADD SET_PY
GET_PZ GET_VZ GET_DT MUL ADD SET_PZ

CONST 1 GET_AGE GET_LIFE DIV SUB SET_PA
```

The `start:` section places each particle at the emitter origin with a random offset of ±16 units, gives it a random velocity up to ±100, sets the size to 6 and alpha to 1. The `update:` section moves each particle by its velocity scaled by delta time and fades alpha to 0 over its lifetime.

### Screen Distortion (screen effect)

```
update:
GET_EY CONST 25 MUL GET_TIME CONST 4 MUL ADD SIN
GET_TX CONST 10 MUL MUL
GET_EX ADD SET_SX
GET_EY SET_SY
SAMPLE
GET_SR SET_PR
GET_SG SET_PG
GET_SB SET_PB
GET_SA SET_PA
```

This screen effect samples the screen with a horizontal sine wave offset based on the V coordinate and time, creating a wavy distortion.

## Loading and Playing

```lua
load_pfx("explosion.pfx")

-- Spawn as particles
particles.spawn("explosion.pfx", origin, 2.0, 32, direction)

-- Play as screen effect
screen.play_effect("distortion.pfx", 3.0)
```
