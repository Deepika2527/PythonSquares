admin = True
role = ["Hr","Manger","Admin"]

if "admin" in role and admin:
    print("Authorised person")
elif "hr" in role:
    print("Only restricted access")
elif "Manager" in role:
    print("Limited access")
else:
    print("Denied")




marks = 99

if marks <= 35:
    print("just passed")
elif marks > 35 and marks < 60:  # Fixed: Catches the gap between 35 and 60
    print("B")
elif marks >= 60 and marks < 80:  # Kept exactly as you wrote it
    print("A")
elif marks >= 80 and marks <= 100:  # Fixed: Upper bound raised to 100 to catch 99
    print("A+")
else:
    print("Failed")


mark = 99

if mark >= 90:
    print("A+")
elif mark >= 80:
    print("A")
elif mark >= 60:
    print("B")
elif mark >= 35:
    print("Just passed")
else:
    print("Failed")
