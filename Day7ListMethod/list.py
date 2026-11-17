l = [1,2,3,4,'Hello',[3,78,'fa'],True,1.7]
print("List:", l)
print("Length of List:", len(l))
print("Postive Inedxing and retrieving the values from index alue", l[0], l[1])
print("Negative Indexing", l[-1])
print(l[-1] , ":",l[-8])
# print(l[8])
# print(l[-9])

print([1,2,4]+[1,2,4])
print([1,2]*3)
print([1,2] in[[1,2],3])
print([1,2] == [1,2])
print([1,2] is [1,2])
a= [1,2]
b = [1,2]
c= a
print(a is b)
print(a is c)
print(b is c)