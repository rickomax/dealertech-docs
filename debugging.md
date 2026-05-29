---
layout: default
title: Debugging with ZeroBrane Studio
nav_order: 3
---

# Debugging Lua with ZeroBrane Studio

This guide explains how to attach the [ZeroBrane Studio](https://studio.zerobrane.com/) Lua debugger to the engine so you can set breakpoints, step through scripts, and inspect variables while the game runs.

## When the debugger is available

- **Inside the Unity Editor** — the debugger is **always enabled** for runs started from the Editor. No extra flags are required.
- **Standalone builds** — you must create a **Development Build** from Unity and launch the game with the `-luadebug` command line argument:

  ```
  DealerTech.exe -luadebug
  ```

> **Warning:** Development Builds should **never be shipped**. They enable unsafe Lua methods and are **not sandboxed** the way standalone (non-development) builds are. Only distribute regular, non-development builds to players.

## Setting up ZeroBrane Studio

1. **Open ZeroBrane Studio.**

2. **Locate the Lua scripts directory.** Copy the full path to `StreamingAssets/Lua`:
   - For a **Unity project**, this is relative to the project root (e.g. `Assets/StreamingAssets/Lua`).
   - For a **player build**, it is generally found under the `DealerTech_Data` folder (e.g. `DealerTech_Data/StreamingAssets/Lua`).

3. **Point the project at that directory.** In the **Project** tab, right-click on the project folder and choose **Edit Project Directory**. Paste the copied path and press <kbd>Enter</kbd>.

4. **Start the debugger server.** From the menu, click **Project → Start Debugger Server**.

## Starting a debugging session

1. Make sure the debugger server is running (see the step above).
2. **Run the game normally:**
   - From the **Unity Editor** — just press Play.
   - From a **standalone Development Build** — launch it with the `-luadebug` argument.

Once the game connects, execution will pause at any breakpoints you set in ZeroBrane Studio, and you can step through code, inspect locals, and evaluate expressions.

## Tips

- Set breakpoints in ZeroBrane *before* (or while) the game is running — the debugger attaches at runtime.
- If the game does not connect, double-check that the project directory in ZeroBrane points at the exact `StreamingAssets/Lua` folder the game is loading from, and that the debugger server was started before the script you want to break in executes.
