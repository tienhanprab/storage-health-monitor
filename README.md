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
+--------------------------+
|        Start             |
+------------+-------------+
             |
             v
+--------------------------+
| Run: diskutil list       |
| Detect physical disks    |
+------------+-------------+
             |
             v
+--------------------------+
| For each physical disk   |
+------------+-------------+
             |
             v
+--------------------------+
| Attempt SMART detection  |
| (smartctl probing)       |
+------------+-------------+
             |
             v
        +----+----+
        | SMART ? |
        +----+----+
             |
     +-------+-------+
     |               |
     v               v
+------------+   +----------------------+
| SMART Mode |   | SMART Unavailable    |
| Detected   |   | (USB / Limitation)   |
+------+-----+   +----------+-----------+
       |                    |
       v                    v
+-------------+    +--------------------+
| Parse SMART |    | Indirect Health    |
| Data        |    | Check              |
| (NVMe/ATA)  |    | - Disk usage       |
+------+------|    | - I/O latency      |
       |           | - OS indicators    |
       |           +---------+----------+
       |                     |
       +----------+----------+
                  |
                  v
+--------------------------+
| Calculate Health Score   |
| (Normalize to 0–100)     |
+------------+-------------+
             |
             v
+--------------------------+
| Assign Health Status     |
| HEALTHY / WARNING /     |
| CRITICAL                 |
+------------+-------------+
             |
             v
+--------------------------+
| Build Unified Report     |
| (JSON / CLI Output)     |
+------------+-------------+
             |
             v
+--------------------------+
|            End           |
+--------------------------+
