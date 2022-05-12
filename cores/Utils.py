from datetime import datetime, time as datetime_time, timedelta

def time_diff(start, end) -> timedelta:
    if isinstance(start, datetime_time):
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end:
        return end - start
    else:
        end += timedelta(1)
        assert end > start
        return end - start
        