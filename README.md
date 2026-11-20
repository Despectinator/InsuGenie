# InsuGenie

InsuGenie is an AI-powered diabetes management platform that combines camera
capture, face-region analysis, remote photoplethysmography, signal processing,
and machine learning to support glucose-related insight workflows.

The repository includes `rPPG-Toolbox` as a third-party research dependency. It
is intentionally kept separate from InsuGenie application code and should be
integrated only through application-owned wrapper modules.

## Features

- Camera capture pipeline
- Face detection and future landmark support
- ROI extraction boundary for rPPG analysis
- Placeholder rPPG wrapper for clean external-toolbox integration
- AI glucose estimation module structure
- Backend API module structure
- Database module structure
- Dashboard module structure

## Directory Structure

```text
InsuGenie/
├── app/
│   ├── ai/
│   ├── backend/
│   ├── camera/
│   ├── config/
│   ├── database/
│   ├── rppg/
│   ├── services/
│   ├── ui/
│   ├── utils/
│   └── main.py
├── dataset/
├── docs/
├── models/
├── tests/
├── rPPG-Toolbox/
├── requirements_insugenie.txt
├── requirements_rppg.txt
├── README.md
└── .gitignore
```

## Installation

Create a dedicated environment for InsuGenie:

```bash
python -m venv venv_insugenie
```

Activate it on Windows PowerShell:

```powershell
.\venv_insugenie\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source venv_insugenie/bin/activate
```

Install InsuGenie dependencies:

```bash
pip install -r requirements_insugenie.txt
```

Create a separate environment for the external rPPG toolbox:

```bash
python -m venv venv_rppg
```

Activate it on Windows PowerShell:

```powershell
.\venv_rppg\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source venv_rppg/bin/activate
```

Install rPPG toolbox dependencies:

```bash
pip install -r requirements_rppg.txt
```

On Windows, this installs the toolbox's base dependencies and skips the
PhysMamba-only native packages that fail during native Windows installation.
Use `requirements_rppg_full.txt` from WSL/Linux if you specifically need
PhysMamba.

## Development Roadmap

- Finalize camera capture and face detection pipeline
- Add landmark detection and ROI extraction
- Validate rPPG-Toolbox runtime requirements in its own environment
- Implement `app/rppg/wrapper.py` as the integration boundary
- Add signal-processing and quality-metric modules
- Build AI glucose estimation feature pipeline
- Add FastAPI backend endpoints
- Add database models and persistence services
- Build the dashboard workflow
- Add automated tests for each application module
