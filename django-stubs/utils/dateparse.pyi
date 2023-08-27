from datetime import date, datetime, time, timedelta
from typing import Any

date_re: Any
time_re: Any
datetime_re: Any
standard_duration_re: Any
iso8601_duration_re: Any
postgres_interval_re: Any

def parse_date(value: str) -> date | None: ...
def parse_time(value: str) -> time | None: ...
def parse_datetime(value: str) -> datetime | None: ...
def parse_duration(value: str) -> timedelta | None: ...
