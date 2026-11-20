# Project Structure

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

## Folders

`app/` contains all InsuGenie application source code.

`app/ai/` contains glucose estimation models, feature preparation, and
prediction logic.

`app/backend/` contains API entry points and backend-facing application code.

`app/camera/` contains camera capture, face detection, landmark detection, and
ROI selection modules.

`app/config/` contains application configuration helpers and settings.

`app/database/` contains persistence models and database access code.

`app/rppg/` contains the InsuGenie-owned rPPG integration boundary, signal
objects, and processing code.

`app/services/` contains orchestration logic that coordinates camera, rPPG, AI,
backend, and database workflows.

`app/ui/` contains dashboard and user interface code.

`app/utils/` contains shared helper functions that do not belong to a specific
domain module.

`dataset/` is reserved for project datasets and local data references.

`docs/` contains architecture, setup, and project documentation.

`models/` stores InsuGenie-owned model files or metadata. Large model artifacts
should not be committed unless explicitly intended.

`tests/` contains automated tests for InsuGenie code.

`rPPG-Toolbox/` is a third-party external research repository. Do not modify its
source code from the InsuGenie application.
