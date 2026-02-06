"""Unified report generation."""

from typing import Any, Dict, List


def _status_for_score(score: int) -> str:
    if score >= 80:
        return "HEALTHY"
    if score >= 50:
        return "WARNING"
    return "CRITICAL"


def build_report(reports: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Render a report with both JSON payload and CLI table."""
    headers = ["Disk", "Mode", "Score", "Confidence", "Status"]
    rows = []
    for report in reports:
        score = int(report.get("health_score", 0))
        confidence = report.get("confidence", 0.0)
        confidence_str = f"{confidence:.2f}"
        rows.append(
            [
                report.get("disk", ""),
                report.get("mode", ""),
                str(score),
                confidence_str,
                report.get("status", _status_for_score(score)),
            ]
        )

    widths = [len(header) for header in headers]
    for row in rows:
        for idx, value in enumerate(row):
            widths[idx] = max(widths[idx], len(value))

    def fmt_row(values: List[str]) -> str:
        return " | ".join(value.ljust(widths[idx]) for idx, value in enumerate(values))

    header_line = fmt_row(headers)
    separator = "-+-".join("-" * width for width in widths)
    table_lines = [header_line, separator]
    for row in rows:
        table_lines.append(fmt_row(row))

    return {
        "table": "\n".join(table_lines),
        "json": reports,
    }
