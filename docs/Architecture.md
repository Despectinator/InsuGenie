# Architecture

InsuGenie follows a clean integration approach: application modules own their
interfaces, and third-party research code is kept behind explicit wrappers.

## Processing Flow

```text
Camera
  |
  v
Face Detection
  |
  v
ROI Extraction
  |
  v
rPPG Engine
  |
  v
Signal Processing
  |
  v
AI Glucose Estimation
  |
  v
Backend
  |
  v
Database
  |
  v
Dashboard
```

## Module Responsibilities

Camera captures frames from the user device.

Face Detection identifies the face region and provides stable tracking inputs.

ROI Extraction selects facial regions suitable for remote photoplethysmography.

rPPG Engine is the integration boundary for pulse-signal extraction. The
third-party toolbox must remain external and should be accessed through
`app/rppg/wrapper.py`.

Signal Processing cleans, normalizes, and transforms raw rPPG outputs into
features usable by downstream models.

AI Glucose Estimation uses processed features to estimate glucose-related
signals or risk indicators.

Backend exposes application workflows through API endpoints.

Database persists user data, measurements, predictions, and audit metadata.

Dashboard presents readings, trends, and user-facing insights.
