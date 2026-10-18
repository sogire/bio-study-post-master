# Workspace Rules

## `uv` Python Package Manager

- **Already Installed**: `uv` is pre-installed on this machine at `/home/sergiobermudez/.local/bin/uv`.
- **Do Not Reinstall**: Never attempt to install or reinstall `uv` (e.g., via `curl -LsSf https://astral.sh/uv/install.sh | sh`). Skip the installation steps in the `uv` skill.
- **Sandbox Visibility**: Because `/home/sergiobermudez/.local/bin/uv` (along with `~/.cache/uv` and `~/.local/share/uv`) is outside the workspace directory, running `uv` inside the default terminal sandbox (`BypassSandbox: false`) may fail with `No such file or directory`. This does **not** mean `uv` is missing—invoke `/home/sergiobermudez/.local/bin/uv` (or `uv`) with `BypassSandbox: true` when executing `uv` commands.

## PyMOL (`pymol`)

- **Already Installed & Cached**: PyMOL is ready to use without installing any system packages (`apt`), `conda` environments, or `pip` packages:
  - **CLI Wrapper**: `/home/sergiobermudez/.local/bin/pymol` (wraps `uv run --with pymol-open-source-whl --with PyQt5 python3 -m pymol "$@"`).
  - **Headless Scripting (`pymol` skill)**: `pymol-open-source-whl` (PyMOL 3.2.0a with OSMesa software rendering) is already cached in `uv`. Run PyMOL scripts directly via `/home/sergiobermudez/.local/bin/uv run <script.py>` using PEP 0723 inline script metadata (`requires-python = ">=3.10, <3.13"`, `dependencies = ["pymol-open-source-whl"]`) and `PYOPENGL_PLATFORM=osmesa`.
- **Do Not Install**: Never attempt to install PyMOL via `apt`, `pip`, or `conda`. Always run PyMOL scripts via `/home/sergiobermudez/.local/bin/uv run` (or `/home/sergiobermudez/.local/bin/pymol`) with `BypassSandbox: true`.

