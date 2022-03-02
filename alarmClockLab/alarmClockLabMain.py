from alarm_clock import AlarmClock

my_bedside_alarm = AlarmClock('12:00pm', True, '5:00am')
print(f'The current time is {my_bedside_alarm.current_time}')
print(f'My alarm is set to {my_bedside_alarm.time_alarm_goes_off}')
if my_bedside_alarm.alarm_clock_on == True:
    print(f'And my alarm is on')
else:
    print(f'And my alarm is off')

my_bedside_alarm.change_time('4:20pm')
my_bedside_alarm.alarm_on_off_switch(False)
print(f'The current time is {my_bedside_alarm.current_time}')
print(f'My alarm is set to {my_bedside_alarm.time_alarm_goes_off}')
if my_bedside_alarm.alarm_clock_on == True:
    print(f'And my alarm is on')
else:
    print(f'And my alarm is off')