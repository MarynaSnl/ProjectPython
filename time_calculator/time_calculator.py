import re
from datetime import  timedelta, datetime, time


def add_time(start, duration, day_week = None):
    if day_week != None:
        day_week = day_week.lower().title()
    s1 = re.findall('[0-9]+', start) + re.findall('[AMPM]+', start)
    s2 =  re.findall('[0-9]+', duration) 
    time_pm_am = (lambda x,y: int(x)+12 if y == 'PM' else int(x))
    d_t = datetime.combine(datetime.now().date(), time(time_pm_am(s1[0], s1[2]) ,int(s1[1])))
    delta = timedelta(hours=int(s2[0]), minutes=int(s2[1]), seconds=0)

    d_t_new = d_t + delta
    days_delta = (d_t_new.date() - d_t.date()).days
    d_t_new_time = d_t_new.time()
    
    d_t_new_day = ''
    if day_week != None:
        d_t_new_day = next_day_week(day_week, days_delta) 
    #d_t_new_day = d_t_new.strftime('%A')

    
    new_time_str = ' ' +str(d_t_new_time.strftime("%I:%M:%p")).replace(':PM', ' PM').replace(':AM', ' AM')
    new_time_str = new_time_str.replace(' 0','')
    if day_week != None:
        new_time_str = new_time_str + ', ' + d_t_new_day.strip().title() + ' '
    if days_delta == 1:
        new_time_str = new_time_str.rstrip() + ' (next day)'
    elif days_delta > 1:
        new_time_str = new_time_str.rstrip() + ' (' + str(days_delta).strip() + ' days later)'
    new_time = new_time_str.strip()   
    return new_time 

def next_day_week(day_week, days_delta):
    d_w = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday' , 'Sunday']
    try:
        pozition_t_d = d_w.index(day_week.lower().title())
    except:
        return ""
    if days_delta > 7:
        days_delta = days_delta%7 
    if days_delta < 7 - pozition_t_d:
        return(d_w[days_delta + pozition_t_d])
    else:
        return(d_w[days_delta + pozition_t_d-7])
    