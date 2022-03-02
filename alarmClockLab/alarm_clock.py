class AlarmClock:

    def __init__(self, pass_current_time, pass_alarm_on, pass_set_alarm_time):
        self.current_time = pass_current_time
        self.alarm_clock_on = pass_alarm_on
        self.time_alarm_goes_off = pass_set_alarm_time

    def change_time(self, changed_time):
        self.current_time = changed_time
        print(self.current_time)

    def alarm_on_off_switch(self, true_on_false_off):
        self.alarm_clock_on = true_on_false_off

    def change_alarm_time(self, changed_time):
        self.time_alarm_goes_off = changed_time
        print(self.time_alarm_goes_off)



