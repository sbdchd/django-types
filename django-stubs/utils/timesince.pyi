from datetime import date
from typing import Any, Optional

TIME_STRINGS: dict[str, str]
TIMESINCE_CHUNKS: Any

def timesince(
    d: date,
    now: Optional[date] = ...,
    reversed: bool = ...,
    time_strings: Optional[dict[str, str]] = ...,
) -> str: ...
def timeuntil(
    d: date, now: Optional[date] = ..., time_strings: Optional[dict[str, str]] = ...
) -> str: ...
