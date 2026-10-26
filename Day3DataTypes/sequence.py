l = [1,2,4,1,2,4,'klp',True,98.8]
print(l)
print(type(l))

print(l[0])
l[0]= 100
print(l)

import sys
print("-------------------------------------------")
t = (1,2,3,True,23+8j,[1,2],1)
print(t)
print(type(t))
print(sys.getsizeof(t))
print(t[1])
# t[1] = 20
# print(t)
#It is immutable
print("---------------------------------------------")

s = "Raghav"
print(s)
print(type(s))
print(s[0])
# s[0] = 'r'
# print(s)
# immtuable

st= 'raghavendra'
print(st)

strn = '''Hello'''
print(strn)
print(type(strn))


print("----------------------------------------------------")

dictn = {
    "name" : "Deepika",
    "age" :25,
    "Role" : "Developer_Trainer",

    

}
print(dictn)
print(type(dictn))

ditn = {
    "name" : "Deepika",
    "age" :25,
    "Role" : "Developer_Trainer",
        (1,2,3) : "list",
        (2,9) : "tuple",
        # {1,3} : "set",
        "dictn" : {
            "skills" : 'html,css',
            "bskills" : 'python,advpython'
        }

    

}
print(ditn)
print(type(ditn))
'''Note you cant use list/set as key in dictionary because they are mutable and hashable but you can use tuple as key because it is immutable and hashable'''


