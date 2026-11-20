# Environment Setup

InsuGenie keeps the application environment separate from the rPPG research
toolbox environment.

## Why Two Virtual Environments Are Needed

`rPPG-Toolbox` is a third-party research repository. Research projects often
pin package versions, depend on specific CUDA or PyTorch combinations, and may
change independently from the application. Keeping it isolated prevents those
dependencies from breaking the InsuGenie backend, dashboard, database layer, or
AI estimation modules.

## InsuGenie Environment

Use this environment for all InsuGenie application code:

```bash
python -m venv venv_insugenie
```

Install application dependencies with:

```bash
pip install -r requirements_insugenie.txt
```

This environment owns:

- Camera capture and face detection
- ROI extraction
- Backend API
- Database access
- Dashboard code
- AI glucose estimation code

## rPPG-Toolbox Environment

Use this environment only for running or validating the external toolbox:

```bash
python -m venv venv_rppg
```

Install toolbox dependencies with:

```bash
pip install -r requirements_rppg.txt
```

On Windows, `requirements_rppg.txt` installs the toolbox's base dependencies
without the PhysMamba-only native packages `causal-conv1d` and `mamba-ssm`.
Those packages build against PyTorch/CUDA tooling and the upstream toolbox
recommends WSL for Windows users.

If you specifically need PhysMamba, use WSL/Linux and install the full upstream
profile instead:

```bash
pip install torch torchvision
pip install -r requirements_rppg_full.txt
```

## How the Two Communicate

The intended integration boundary is `app/rppg/wrapper.py`.

For now, the wrapper is a placeholder and does not import the toolbox. Later,
InsuGenie should pass prepared ROI frame sequences into the wrapper and receive
application-owned signal objects back. If the two environments cannot safely run
in the same process, the wrapper can communicate with the toolbox through a
separate process, local API, command-line invocation, or serialized files.

TODO: Choose the final communication mechanism after validating toolbox runtime
requirements and expected input/output formats.
