# Austin Daybell
# Blue Moon Activity

BlueMoon = input("Is there a blue moon tonight(Yes or No)? ")
Day_of_week = input("What is the day of the week(Monday-Sunday)? ")
Date_of_month = int(input("What is the day of the month(1-31)? "))

if BlueMoon == "Yes":
    print("""-----------------------------
Play song Once in a Blue Moon
          """)
else:
    print("""---------------------------------- 
You may have a blue moon next time
""")
if Date_of_month <=7:
    if Day_of_week == "Monday":
        print("""Play song Manic Monday
----------------------""")
    elif Day_of_week == "Tuesday":
        print("""Play song Tuesday's Gone
------------------------""")
    elif Day_of_week == "Wednesday":
        print("""Play song Just Wednesday
------------------------""")
    elif Day_of_week == "Thursday":
        print("""Play songSweet Thursday
-----------------------""")
    elif Day_of_week == "Friday":
        print("""Play song Friday I'm in Love
----------------------------""")
    elif Day_of_week == "Saturday":
        print("""Play song Saturday in the Park
------------------------------""")
    elif Day_of_week == "Sunday":
        print("""Play song Lazing on a Sunday Afternoon
--------------------------------------""")
else:
    print("""Play song Day Dream Believer
----------------------------""")
