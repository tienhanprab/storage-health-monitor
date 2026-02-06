# storage-health-monitor (macOS)
This project detects physical disks on macOS and determines whether SMART data is available. 
External USB drives may not expose SMART data due to bridge limitations on macOS. 
The system detects SMART availability and adapts health checks accordingly.

## Features
- Automatic detection of physical disks
- SMART capability detection
- NVMe SMART health analysis
- Graceful degradation for USB drives without SMART
- Unified health score (0-100)

## Why SMART May Be Unavailable
External USB drives often do not expose SMART data due to USB bridge limitations on macOS.

## Health Scoring
- SMART-based: temperature, wear level, error counters
- Non-SMART: disk usage, I/O latency, OS-level indicators

## Architecture Diagram

<p align="center"><img src="images/SMART Disk Health Pipeline.png" width="500"></p>

## Images

All project images are stored in the [`images`](images/) folder.

## Project Structure

```
storage-health-monitor/
│
├── main.py                 # entry point
├── disk_detector.py        # list physical disks
├── smart_checker.py        # SMART detection + parsing
├── indirect_health.py      # non-SMART health check
├── health_score.py         # scoring logic
├── report.py               # unified report
├── README.md
└── images
```
