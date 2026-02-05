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

+----------------------+
|   diskutil list      |
|  (macOS Native Tool) |
+----------+-----------+
           |
           v
+----------------------+
|   Disk Detector      |
|  (Physical Disks)    |
+----------+-----------+
           |
           v
+------------------------------+
| SMART Capability Detector    |
+----------+-------------------+
           |
     +-----+-----+
     |           |
     v           v
+-----------+  +--------------------+
| SMART OK  |  | SMART UNAVAILABLE  |
+-----+-----+  +---------+----------+
      |                  |
      v                  v
+-------------+   +-------------------+
| SMART Health |   | Indirect Health   |
| Analyzer    |   | Analyzer          |
+------+------|   +---------+---------+
       \                  /
        \                /
         v              v
     +------------------------+
     | Health Scoring Engine  |
     |    (0–100 Score)       |
     +-----------+------------+
                 |
                 v
     +------------------------+
     | Unified Health Report  |
     |  Status + Diagnostics  |
     +------------------------+
