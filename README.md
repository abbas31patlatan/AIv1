# AIv1 Sample Project

This repository provides a minimal example of how the various modules could integrate to form a basic AI system. The goal is to demonstrate simple memory storage, NLP utilities, and task scheduling. The code is intentionally lightweight so it can run in restricted environments.

The NLP package now contains a handful of additional utilities such as a
politeness filter, slang normaliser and a tiny rule based translator. These
modules show how a dialogue pipeline could be composed from small, testable
building blocks. The system also demonstrates loading modern `gguf` language
models via the optional ``llama_cpp`` wrapper.

The GUI has also been fleshed out with a minimal configuration menu. Users can
toggle voice feedback, switch between one of the predefined themes and enable or
disable offline mode. Preferences are persisted across runs in
``gui_prefs.json`` within the configured data directory.

## Quick Start

```bash
python main.py
