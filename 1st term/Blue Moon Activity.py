# Austin Daybell
# Blue Moon Activity

yes_or_no = "Yes, yes"
dayOfSunday = "Sunday, sunday"
dayOfSaturday = "Saturday, saturday"
dayOfFriday = "Friday, friday"
dayOfThursday = "Thursday, thursday"
dayOfWednesday = "Wednesday, wednesday"
dayOfTuesday = "Tuesday, tuesday"
dayOfMonday = "Monday, monday"

BlueMoon = input("Is there a blue moon tonight(Yes or No)? ")
Day_of_week = input("What is the day of the week(Monday-Sunday)? ")
Date_of_month = int(input("What is the day of the month(1-7)? "))

if BlueMoon in yes_or_no:
    print("""-----------------------------
Play song Once in a Blue Moon
          """)
else:
    print("""---------------------------------- 
You may have a blue moon next time
""")
if Date_of_month <=7:
    if Day_of_week in dayOfMonday:
        print("""Play song Manic Monday
----------------------""")
    elif Day_of_week in dayOfTuesday:
        print("""Play song Tuesday's Gone
------------------------""")
    elif Day_of_week in dayOfWednesday:
        print("""Play song Just Wednesday
------------------------""")
    elif Day_of_week in dayOfThursday:
        print("""Play songSweet Thursday
-----------------------""")
    elif Day_of_week in dayOfFriday:
        print("""Play song Friday I'm in Love
----------------------------""")
    elif Day_of_week in dayOfSaturday:
        print("""Play song Saturday in the Park
------------------------------""")
    elif Day_of_week in dayOfSunday:
        print("""Play song Lazing on a Sunday Afternoon
--------------------------------------""")
else:
    print("""Play song Day Dream Believer
----------------------------""")
