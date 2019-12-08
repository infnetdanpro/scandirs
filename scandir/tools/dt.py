from datetime import datetime


def timestamp_to_str(tstamp: int) -> str:
    dt = datetime.fromtimestamp(tstamp)
    return dt.strftime('%Y.%m.%d %H:%M:%S')
