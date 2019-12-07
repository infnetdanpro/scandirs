from datetime import datetime


def timestamp_to_str(tstamp):
    dt = datetime.fromtimestamp(tstamp)
    return dt.strftime('%Y.%m.%d %H:%M:%S')
