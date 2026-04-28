---
layout: default
title: globals
parent: API Reference
---

# `globals`

Lua globals registered in `LuaInterface.SetupEnvironment` and refreshed each frame in `LuaInterface.UpdateEnvironment`.

## Global functions and objects

- `load_bsp` → `new LuaFunction(BSPLoader.LoadBSP)`
- `load_mdl` → `new LuaFunction(MDLLoader.LoadMDL)`
- `load_wav` → `new LuaFunction(WAVLoader.LoadWAV)`
- `load_png` → `new LuaFunction(PNGLoader.LoadPNG)`
- `load_pfx` → `new LuaFunction(PFXLoader.LoadPFX)`
- `host` → `new LuaFunction(NetworkController.Host)`
- `connect` → `new LuaFunction(NetworkController.Connect)`
- `run` → `new LuaFunction(RunScript)`
- `quit_game` → `new LuaFunction(GameController.Quit)`
- `config` → `new LuaConfig()`
- `bsp` → `new LuaBSP()`
- `entity` → `new GameObject("DummyGameEntity").AddComponent<GameEntity>()`
- `input` → `new LuaInput()`
- `math` → `new LuaMath()`
- `vector` → `new LuaVector()`
- `vector4` → `new LuaVector4()`
- `physics` → `new LuaPhysics()`
- `particles` → `new LuaParticles()`
- `lights` → `new LuaLights()`
- `input_data` → `new LuaInputData()`
- `movement_data` → `new LuaMovementData()`
- `entity_state` → `new LuaEntityState()`
- `array` → `new LuaArray()`
- `font` → `new LuaFont()`
- `ui_panel` → `new LuaUIPanel()`
- `ui_label` → `new LuaUILabel()`
- `ui_input_field` → `new LuaUIInputField()`
- `ui_image` → `new LuaUIImage()`
- `unload_ui` → `new LuaFunction(GameController.UnloadUI)`
- `move_type` → `new LuaMoveType()`
- `solid` → `new LuaSolid()`
- `screen` → `new LuaScreen()`
- `frame_time` → `NetworkController.Instance.DeltaTime`
- `time` → `NetworkController.Instance.ServerTime` (refreshed each frame)
- `me` → the Lua instance table of the local player (set via `LuaInterface.SetMe` after player spawn)
