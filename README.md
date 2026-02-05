# storage-health-monitor (macOS)
This project detects physical disks on macOS and determines whether SMART data is available.

## Features
- Automatic detection of physical disks
- SMART capability detection
- NVMe SMART health analysis
- Graceful degration for USB drives without SMART
- Unified health score (0-100)

## Why SMART May Be Unavailable
External USB drives often do not expose SMART data due to USB bridge limitations on macOS.

## Health Scoring
- SMART-based: temperature, wear level, error counters
- Non-SMART: disk usage, I/O latency, OS-level indicators

## Architecture Diagram

```mermaid
flowchart TD
    A[diskutil list<br/>(macOS Native Tool)] --> B[Disk Detector<br/>(Physical Disks)]
    B --> C[SMART Capability Detector]
    C --> D[SMART OK]
    C --> E[SMART UNAVAILABLE]
    D --> F[SMART Health Analyzer]
    E --> G[Indirect Health Analyzer]
    F --> H[Health Scoring Engine<br/>(0–100 Score)]
    G --> H
    H --> I[Unified Health Report<br/>Status + Diagnostics]
```

