a = 10
print(a)

print(type(a))
b = a
print(b)
print(id(a))
print(id(b))

del a
# print(a)
print(b)

# print(id(a))
print(id(b))



import keyword
print(keyword.kwlist)