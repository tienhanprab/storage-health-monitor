"""Non-SMART health checks (usage, latency, OS indicators)."""

from typing import Any, Dict
import os
import shutil
import time


def get_indirect_health(disk: str, mount_point: str = "/") -> Dict[str, Any]:
    """Return indirect health signals for a disk."""
    usage = shutil.disk_usage(mount_point)
    score = 100

    if usage.free / usage.total < 0.1:
        score -= 30

    test_file = "/tmp/disk_test.tmp"
    start = time.time()
    with open(test_file, "w", encoding="utf-8") as handle:
        handle.write("test" * 100000)
    elapsed = time.time() - start
    os.remove(test_file)

    if elapsed > 0.5:
        score -= 20

    return {
        "method": "INDIRECT",
        "score": score,
        "io_latency": elapsed,
        "mount_point": mount_point,
        "disk": disk,
    }
