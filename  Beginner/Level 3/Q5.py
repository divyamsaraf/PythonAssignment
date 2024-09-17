class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, other_time):
        total_minutes = (self.hours * 60 + self.minutes) + (other_time.hours * 60 + other_time.minutes)
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)
    
    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")
    
    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minutes")

def get_time_input(prompt):
    while True:
        try:
            hours = int(input(f"Enter the hours for {prompt}: "))
            minutes = int(input(f"Enter the minutes for {prompt}: "))
            if hours < 0 or minutes < 0 or minutes >= 60:
                raise ValueError("Invalid input: minutes should be between 0 and 59.")
            return Time(hours, minutes)
        except ValueError as e:
            print(e)
            print("Please enter valid integers. Minutes should be between 0 and 59.")

print("Enter details for the first time: ")
time1 = get_time_input("first time")
    
print("\nEnter details for the second time: ")
time2 = get_time_input("second time")
    
result_time = time1.addTime(time2)
    
print("\nFirst Time:")
time1.displayTime()
time1.displayMinutes()
    
print("\nSecond Time:")
time2.displayTime()
time2.displayMinutes()
    
print("\nResult Time:")
result_time.displayTime()
result_time.displayMinutes()