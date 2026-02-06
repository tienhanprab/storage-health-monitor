"""Entry point for storage health monitoring."""

import json

from disk_detector import list_physical_disks
from smart_checker import parse_smart_health, try_smart
from indirect_health import get_indirect_health
from health_score import calculate_health_score
from report import build_report


def main() -> None:
    disks = list_physical_disks()
    reports = []

    for disk in disks:
        smart_ok, output = try_smart(disk)

        if smart_ok:
            data = parse_smart_health(output)
            score, confidence = calculate_health_score(smart=data, indirect=None)
            report = {
                "disk": disk,
                "mode": "SMART",
                "health_mode_reason": "SMART data available via smartctl",
                "health_score": score,
                "confidence": confidence,
                "status": "HEALTHY" if score >= 80 else "WARNING" if score >= 50 else "CRITICAL",
                "details": data,
            }
        else:
            indirect = get_indirect_health(disk)
            score, confidence = calculate_health_score(smart=None, indirect=indirect)
            report = {
                "disk": disk,
                "mode": "INDIRECT_ONLY",
                "health_mode_reason": "SMART unavailable; using indirect checks",
                "health_score": score,
                "confidence": confidence,
                "status": "HEALTHY" if score >= 80 else "WARNING" if score >= 50 else "CRITICAL",
                "details": indirect,
            }

        reports.append(report)

    output = build_report(reports)
    print(output["table"])
    print()
    print(json.dumps(output["json"], indent=2))


if __name__ == "__main__":
    main()
