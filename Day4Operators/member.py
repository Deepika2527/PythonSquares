a =  123
b = 123
print(a is b)



c= 1234
d = 12345

print(c is d)


courses = ["Python", "HTML", "CSS", "JavaScript"]

print("Python" in courses)      # True
print("Java" not in courses)    # True

requested_course = "Python"

if requested_course in courses:
    print("Course available")
else:
    print("Course unavailable")


student = {"name": "Ravi", "course": "Python"}

print("name" in student)  # True
print("Ravi" in student)  # False




list1 = [10, 20]
list2 = [10, 20]
list3 = list1

print(list1 == list2)  # True
print(list1 is list2)  # False
print(list1 is list3)  # True
'''list1 == list2: the contents are equal.



list1 is list2: they are two separate list objects.



list1 is list3: both names refer to the same list object.'''