import datetime

ZERO = datetime.timedelta(0)

class FixedOffsetTimezone(datetime.tzinfo): ...  # type: ignore[misc]

STDOFFSET: datetime.timedelta
DSTOFFSET: datetime.timedelta
DSTDIFF: datetime.timedelta

class LocalTimezone(datetime.tzinfo): ...  # type: ignore[misc]

LOCAL: LocalTimezone
