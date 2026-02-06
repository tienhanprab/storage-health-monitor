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

![Architecture Diagram](images/architecture.png)

## Images

All project images are stored in the [`images`](images/) folder.

### Image References

To reference images in markdown, use the following syntax:

```markdown
![Alt text](images/image-name.png)
```

Examples:
```markdown
![Storage Health Monitor Flow](images/storage-flow.png)
![SMART Data Structure](images/smart-structure.png)
![Disk Detection Process](images/detection-process.png)
```
