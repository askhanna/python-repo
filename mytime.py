class Time:
    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds  = seconds

    def display(self):
        print("The time is {}:{}:{}".format(self.hours,self.minutes,self.seconds))

    

