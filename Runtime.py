__all__ = ['Runtime']

k_min = 60
k_hour = k_min*k_min
k_day = k_hour*24

def _Pluralize(s, pluralize):
    if pluralize:
        return '%ss' % s
    return s

def _Seconds(seconds, secString, pluralize):
    if seconds == 0:
        return ''
    if seconds == 1:
        return '1 %s' % secString
    return '%d %s' % (seconds, _Pluralize(secString, pluralize))

def _Minute(seconds, secString, minString, pluralize):
    if seconds == k_min:
        return '1 %s' % minString
    minutes = int(seconds/float(k_min))
    newSeconds = seconds-minutes*k_min

    if minutes > 1:
        minString = _Pluralize(minString, pluralize)

    output = ''
    if minutes > 0:
        output = '%d %s' % (minutes, minString)
    if newSeconds > 0:
        output = '%s %s' % (output, _Seconds(newSeconds, secString, pluralize))
    return output.strip()

def _Hour(seconds, secString, minString, hourString, pluralize):
    if seconds == k_hour:
        return '1 %s' % hourString
    hours = int(seconds/float(k_hour))
    newSeconds = seconds-hours*k_hour

    if hours > 1:
        hourString = _Pluralize(hourString, pluralize)

    output = ''
    if hours > 0:
        output = '%d %s' % (hours, hourString)
    if newSeconds > 0:
        output = '%s %s' % (output, _Minute(newSeconds, secString, minString, pluralize))
    return output.strip()

def _Day(seconds, secString, minString, hourString, dayString, pluralize):
    if seconds == k_day:
        return '1 %s' % dayString
    days = int(seconds/float(k_day))
    newSeconds = seconds-days*k_day

    if days > 1:
        dayString = _Pluralize(dayString, pluralize)

    output = ''
    if days > 0:
        output = '%d %s' % (days, dayString)
    if newSeconds > 0:
        output = '%s %s' % (output, _Hour(newSeconds, secString, minString, hourString, pluralize))
    return output.strip()

def Runtime(seconds, second='second', minute='minute', hour='hour', day='day', pluralize=True):
    if seconds < k_min:
        return _Seconds(seconds, second, pluralize)
    elif seconds < k_hour:
        return _Minute(seconds, second, minute, pluralize)
    elif seconds < k_day:
        return _Hour(seconds, second, minute, hour, pluralize)
    else:
        return _Day(seconds, second, minute, hour, day, pluralize)
