"""Health score calculation logic."""

from typing import Any, Dict, Optional, Tuple


def _safe_int(value: str, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def calculate_health_score(
    smart: Optional[Dict[str, Any]],
    indirect: Optional[Dict[str, Any]],
) -> Tuple[int, float]:
    """Combine SMART and indirect data into a 0-100 score with confidence."""
    if smart:
        used_raw = str(smart.get("Percentage Used", "0")).replace("%", "")
        used = _safe_int(used_raw, default=0)

        temp_raw = str(smart.get("Temperature", "0")).split()[0]
        temp = _safe_int(temp_raw, default=0)

        media_errors = _safe_int(str(smart.get("Media and Data Integrity Errors", "0")))
        reallocated = _safe_int(str(smart.get("Reallocated_Sector_Ct", "0")))

        score = 100 - used
        if temp > 50:
            score -= 20
        if media_errors > 0:
            score -= 20
        if reallocated > 0:
            score -= 10

        score = max(score, 0)
        confidence = 0.9
        return score, confidence

    if indirect:
        score = max(int(indirect.get("score", 0)), 0)
        confidence = 0.6
        return score, confidence

    return 0, 0.0
