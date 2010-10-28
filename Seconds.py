__all__ = ['Seconds']

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

def Seconds(seconds, formatter, displayZero=False):
    '''
    Return a formatted string for a given number of seconds.
    
    The formatter string specifies how the result is formatted.
        %D = day
        %H = hour
        %M = minute
        %S = seconds
        
        %H hr %M min %S sec
        
    Pluralization can be specified by adding the plural characters in parenthesis at the end of the string.
        %D day(s) %H hour(s) %M minute(s) %S second(s)
        
    Not every element has to be included in the formatter string, if a larger element is excluded the smaller element will collect the over flow.
        26 hours, instead of 1 day 2 hours
        
    By default 0 values are omitted, however passing True to displayZero will include them in the result.
    '''
    values = []
    replace = {
        '%D' : 0,
        '%H' : 0,
        '%M' : 0,
        '%S' : 0,
    }
    parts = k_findParts.findall(formatter)
    partElements = [element[:2] for element in parts]
    
    #Set the element values, we start from smallest to largest
    #so if a larger element isn't specified the smallerone
    #contains the overflow. example: 26 hours, instead of 1 day 2 hours
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
        
        #replace the element key with it's value
        element = k_partElement.match(part)
        if element:
            value = replace.get(element.group(1), 0)
            part = part.replace(element.group(1), str(value))
            
        #determin if the element should be shown
        if not displayZero and value == 0:
            continue
            
        #determin if the element should be plural
        pluralize = k_partPluralize.match(part)
        if pluralize:
            part = part.replace(
                pluralize.group(1), 
                '' if value == 1 else pluralize.group(1)[1:-1]
            )
                
        values.append(part)
        
    return ''.join(values).strip()
