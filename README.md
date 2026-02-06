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

<p align="center"><img src="images/SMART Disk Health Pipeline.png" width="500"></p>

## Images

All project images are stored in the [`images`](images/) folder.
