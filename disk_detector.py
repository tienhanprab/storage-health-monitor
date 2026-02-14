"""Disk detection for macOS physical disks."""

from typing import List
import re
import subprocess


def list_physical_disks() -> List[str]:
    """Return a list of physical disk identifiers (e.g., /dev/disk0)."""
    result = subprocess.run(
        ["diskutil", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []

    disks: List[str] = []
    for line in result.stdout.splitlines():
        lowered = line.lower()
        if "physical" not in lowered:
            continue
        if "synthesized" in lowered:
            continue
        match = re.search(r"(/dev/disk\d+)", line)
        if match:
            disks.append(match.group(1))

    return disks
