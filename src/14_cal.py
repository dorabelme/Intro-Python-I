"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
import re

arg = len(sys.argv)
today = datetime.today()

print(arg)
print(sys.argv)

if arg == 3 and int(sys.argv[1]) > 0 and int(sys.argv[1]) <= 12 and re.search(sys.argv[2], '.*([1-2][0-9]{3})'):
    month = int(sys.argv[1])
    year = int(sys.argv[2])
elif arg == 3 and (int(sys.argv[1]) <= 0 or int(sys.argv[1]) > 12) and len(sys.argv[2]) != 4:
    print("Second argument should be greater than 0 and less than or equal to 12.")
    print("Third argument should be 4 digits long.")
elif arg == 2 and int(sys.argv[1]) > 0 and int(sys.argv[1]) <= 12:
    month = int(sys.argv[1])
    year = today.year
elif arg == 2 and (int(sys.argv[1]) <= 0 or int(sys.argv[1]) > 12):
    print("Second argument should be a number greater than 0 and less than or equal to 12.")
elif arg == 1:
    month = today.month
    year = today.year
else:
    print("Input must have a format [month] [year] in numbers.")
    exit(0)

print(calendar.TextCalendar().formatmonth(year, month))
