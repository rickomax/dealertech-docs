---
layout: default
title: "font.create(filename, image, glyph_size) -> font"
parent: font
grand_parent: API Reference
nav_order: 1
---

# `font.create(filename, image, glyph_size) -> font`

Loads a font asset from a TTF/OTF file in the `fonts` folder, or builds a bitmap font from a texture resource.

**Parameters**
- `filename` (`string|nil`) — Font filename relative to the `fonts` folder. When provided, loaded as a vector font and `image` is ignored.
- `image` (`string|nil`, default `nil`) — Texture resource filename used to build a bitmap font. Only used when `filename` is `nil` or empty.
- `glyph_size` (`integer`, default `8`) — Bitmap glyph size in pixels. Only used when building a bitmap font.

**Returns**
- `font`

**Errors**
- Throws if the font file cannot be found.
- Throws if neither a valid font filename nor a valid bitmap image is provided.

