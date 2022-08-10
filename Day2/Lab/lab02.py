## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return f"{self.hour:02}" + ":" + f"{self.minutes:02}"
    
    ## Add time
    ## Don't return anything
    def __add__(self, minutes):
        if (self.minutes + minutes) < 60:
            print("Add: 1st IF fired")
            self.minutes += minutes
        elif (minutes % 60) == 0:
            print("Add: 2nd IF fired")
            self.hour += ((self.minutes + minutes) // 60)
        elif ((self.minutes + minutes) % 60) == 0:
            print("Add: 3rd IF fired")
            self.minutes = 0
        else:
            print("Add: 4th IF fired")
            self.hour += ((self.minutes + minutes) // 60)
            self.minutes += ((self.minutes + minutes) % 60)
        if self.hour >= 24:
            print("Add: 24 hour IF fired")
            self.hour -= 24
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self, minutes):
        if (self.minutes - minutes) > 0:
            print("Sub: 1st IF fired")
            self.minutes -= minutes
        elif (minutes % 60) == 0:
            print("Sub: 2nd IF fired")
            self.hour -= ((self.minutes - minutes) // 60)
        elif ((self.minutes - minutes) % 60) == 0:
            print("Sub: 3rd IF fired")
            self.minutes = 0
        else:
            print("Sub: 4th IF fired")
            self.hour += ((self.minutes - minutes) // 60)
            self.minutes += ((self.minutes - minutes) % 60)
        if self.hour < 0:
            print("Sub: 24 hour IF fired")
            self.hour += 24
    
    ## Are two times equal?
    def __eq__(self, other):
    
    ## Are two times not equal?
    def __ne__(self, other):


# You should be able to run these
clock1 = Clock(23, 5)
print(clock1) # 23:05
clock2 = Clock(12, 45)
print(clock2) # 12:45
clock3 = Clock(12, 45)
print(clock3) # 12:45

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("testing addition")
clock1 + 60
print(clock1) # 00:05
print(clock1 == Clock(0, 5)) # True

print("testing subtraction")
clock1 - 100
print(clock1) # 22:25