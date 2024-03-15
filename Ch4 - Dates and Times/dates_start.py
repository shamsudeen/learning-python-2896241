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
  
#Your program needs to alert the user if their password expires in less than 7 days
    #You need to get the current date/time using the datetime module
    #You also need to check when the password was last changed - this will be stored in the database as a timestamp
    #You also need to calculate how many days are left until the password expires
    #If there are 7 or fewer days remaining, you should display an urgent message saying so
    #Otherwise, just show a normal message saying how many days are left
    # Assuming the password expiration date is in the texp variable,
 
#   if ((texp-date.today()).days<7):
#     print("password will expire soon!")