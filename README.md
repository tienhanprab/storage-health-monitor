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

## Troubleshooting
- If a disk shows `INDIRECT_ONLY`, the tool automatically falls back to indirect health checks (usage + latency).
- Make sure `smartctl` is installed and available in your `PATH` to enable SMART probing.
- The `__pycache__` folder is normal; Python creates it to speed up future runs.

## Usage

Run:

```bash
python main.py
```

Sample output:

```text
Disk       | Mode          | Score | Confidence | Status
-----------+---------------+-------+------------+--------
/dev/disk0 | SMART         | 98    | 0.90       | HEALTHY
/dev/disk4 | INDIRECT_ONLY | 100   | 0.60       | HEALTHY
/dev/disk6 | INDIRECT_ONLY | 100   | 0.60       | HEALTHY
/dev/disk7 | INDIRECT_ONLY | 100   | 0.60       | HEALTHY
/dev/disk9 | INDIRECT_ONLY | 100   | 0.60       | HEALTHY

[
	{
		"disk": "/dev/disk0",
		"mode": "SMART",
		"health_mode_reason": "SMART data available via smartctl",
		"health_score": 98,
		"confidence": 0.9,
		"status": "HEALTHY",
		"details": {
			"Model Number": "APPLE SSD AP0512Q",
			"Serial Number": "0ba014638010d20e",
			"Firmware Version": "555",
			"PCI Vendor/Subsystem ID": "0x106b",
			"IEEE OUI Identifier": "0x000000",
			"Controller ID": "0",
			"NVMe Version": "<1.2",
			"Number of Namespaces": "3",
			"Local Time is": "Sat Feb  7 00:12:39 2026 +07",
			"Firmware Updates (0x02)": "1 Slot",
			"Optional Admin Commands (0x0004)": "Frmw_DL",
			"Optional NVM Commands (0x0004)": "DS_Mngmt",
			"Maximum Data Transfer Size": "256 Pages",
			"SMART overall-health self-assessment test result": "PASSED",
			"Critical Warning": "0x00",
			"Temperature": "39 Celsius",
			"Available Spare": "100%",
			"Available Spare Threshold": "99%",
			"Percentage Used": "2%",
			"Data Units Read": "94,037,213 [48.1 TB]",
			"Data Units Written": "116,887,113 [59.8 TB]",
			"Host Read Commands": "2,471,052,798",
			"Host Write Commands": "2,259,464,948",
			"Controller Busy Time": "0",
			"Power Cycles": "1,867",
			"Power On Hours": "1,429",
			"Unsafe Shutdowns": "270",
			"Media and Data Integrity Errors": "0",
			"Error Information Log Entries": "0",
			"Read 1 entries from Error Information Log failed": "GetLogPage failed: system=0x38, sub=0x0, code=745"
		}
	},
	{
		"disk": "/dev/disk4",
		"mode": "INDIRECT_ONLY",
		"health_mode_reason": "SMART unavailable; using indirect checks",
		"health_score": 100,
		"confidence": 0.6,
		"status": "HEALTHY",
		"details": {
			"method": "INDIRECT",
			"score": 100,
			"io_latency": 0.00033593177795410156,
			"mount_point": "/",
			"disk": "/dev/disk4"
		}
	},
	{
		"disk": "/dev/disk6",
		"mode": "INDIRECT_ONLY",
		"health_mode_reason": "SMART unavailable; using indirect checks",
		"health_score": 100,
		"confidence": 0.6,
		"status": "HEALTHY",
		"details": {
			"method": "INDIRECT",
			"score": 100,
			"io_latency": 0.0011098384857177734,
			"mount_point": "/",
			"disk": "/dev/disk6"
		}
	},
	{
		"disk": "/dev/disk7",
		"mode": "INDIRECT_ONLY",
		"health_mode_reason": "SMART unavailable; using indirect checks",
		"health_score": 100,
		"confidence": 0.6,
		"status": "HEALTHY",
		"details": {
			"method": "INDIRECT",
			"score": 100,
			"io_latency": 0.0003409385681152344,
			"mount_point": "/",
			"disk": "/dev/disk7"
		}
	},
	{
		"disk": "/dev/disk9",
		"mode": "INDIRECT_ONLY",
		"health_mode_reason": "SMART unavailable; using indirect checks",
		"health_score": 100,
		"confidence": 0.6,
		"status": "HEALTHY",
		"details": {
			"method": "INDIRECT",
			"score": 100,
			"io_latency": 0.00031375885009765625,
			"mount_point": "/",
			"disk": "/dev/disk9"
		}
	}
]
```

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
