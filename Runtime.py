import re

k_min = 60
k_hour = k_min*k_min
k_day = k_hour*24

k_findParts = re.compile('(%[^%]*)')
k_partElement = re.compile('^(%\w)')
k_partPluralize = re.compile('[^\(]*(\(.+\))')

def _Days(seconds):
    days = int(seconds/float(k_day))
    newSeconds = seconds-days*k_day  
    return days, newSeconds
    
def _Hours(seconds):
    hours = int(seconds/float(k_hour))
    newSeconds = seconds-hours*k_hour
    return hours, newSeconds
    
def _Minutes(seconds):
    minutes = int(seconds/float(k_min))
    newSeconds = seconds-minutes*k_min
    return minutes, newSeconds

def Seconds(seconds, string, displayZero=False):
    values = []
    replace = {
        '%D' : 0,
        '%H' : 0,
        '%M' : 0,
        '%S' : 0,
    }
    parts = k_findParts.findall(string)
    partElements = [element[:2] for element in parts]
    
    replace['%S'] = seconds
    if seconds >= k_min and '%M' in partElements:
        minutes, newSeconds = _Minutes(seconds)
        replace['%M'] = minutes
        replace['%S'] = newSeconds
    if seconds >= k_hour and '%H' in partElements:
        hours, newSeconds = _Hours(seconds) 
        replace['%H'] = hours
        minutes, newSeconds = _Minutes(newSeconds)
        replace['%M'] = minutes
        replace['%S'] = newSeconds
    if seconds >= k_day and '%D' in partElements:
        days, newSeconds = _Days(seconds)
        replace['%D'] = days
        hours, newSeconds = _Hours(newSeconds) 
        replace['%H'] = hours
        minutes, newSeconds = _Minutes(newSeconds)
        replace['%M'] = minutes
        replace['%S'] = newSeconds
    
    for part in parts:
        value = 0
        element = k_partElement.match(part)
        if element:
            value = replace.get(element.group(1), 0)
            part = part.replace(element.group(1), str(value))
        if not displayZero and value == 0:
            continue
        pluralize = k_partPluralize.match(part)
        if pluralize:
            if value == 1:
                part = part.replace(pluralize.group(1), '')
            else:
                part = part.replace(pluralize.group(1), pluralize.group(1)[1:-1])
                
        values.append(part)
        
    return ''.join(values).strip()
