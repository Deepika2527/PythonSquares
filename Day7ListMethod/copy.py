a =[1,2,3,4]
b = a
print(a)
print(b)
print(id(a))
print(id(b))
a[2] = -22
print(a)
print(b)
c = [12,3,4,5]
d = c.copy()
print(d)
print(c)
print(id(c))
print(id(d))
c[1]= 100
print(d)
print(c)


