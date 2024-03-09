#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print(f"Today's Date: {today}")

    # TODO: print out the date's individual components
    print("Date components:", today.day, today.month, today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is", today.weekday())
    days = ["mon","tue","wed", "thur", "fri","sat","sun"]
    print("Which is a ", days[today.weekday()])    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("\nCurrent Datetime:", today)

    # TODO: Retrieve the year, month and day from the datetime object
    dt_components = (today.year, today.month, today.day)
    print("Datetime Components:", *dt_components)
    
    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("Current Time:", t)

    # TODO: Compare two datetime objects to see if they represent the same point in time
    d1 = datetime(2007,8,23)
    d2 = datetime(2007,8,23,14,55,36)
    print("\nd1 == d2?", d1==d2)                   # False
    print("d1 <= d2?", d1<=d2)                   #
 

  
if __name__ == "__main__":
    main()
  