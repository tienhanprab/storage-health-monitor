"""SMART capability detection and parsing."""

from typing import Any, Dict, Tuple
import re
import subprocess


def try_smart(disk: str) -> Tuple[bool, str]:
    """Try smartctl probes for a disk and return support plus raw output."""
    cmds = [
        ["smartctl", "-a", disk],
        ["smartctl", "-a", "-d", "nvme", disk],
        ["smartctl", "-a", "-d", "auto", disk],
    ]

    for cmd in cmds:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        output = (result.stdout or "") + (result.stderr or "")
        if "SMART overall-health" in output or "NVMe" in output:
            return True, output
        if "Operation not supported" in output:
            return False, output

    return False, "UNKNOWN"


def parse_nvme_health(output: str) -> Dict[str, Any]:
    """Parse key-value style NVMe SMART data."""
    health: Dict[str, Any] = {}
    for line in output.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            health[key.strip()] = value.strip()
    return health


def parse_ata_health(output: str) -> Dict[str, Any]:
    """Parse ATA SMART attribute table into a dictionary of raw values."""
    health: Dict[str, Any] = {}
    for line in output.splitlines():
        match = re.match(r"\s*\d+\s+([A-Za-z0-9_\-]+)\s+\S+\s+\d+\s+\d+\s+\d+\s+\S+\s+\S+\s+\S+\s+(\S+)", line)
        if match:
            name = match.group(1)
            raw = match.group(2)
            health[name] = raw
    return health


def parse_smart_health(output: str) -> Dict[str, Any]:
    """Parse SMART output for either NVMe or ATA devices."""
    if "NVMe" in output or "Percentage Used" in output:
        return parse_nvme_health(output)
    return parse_ata_health(output)
