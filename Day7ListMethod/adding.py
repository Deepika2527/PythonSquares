l = [1,2,4,5,6]
print(l)
l.append(10)
print(l)
l.extend(["ext1","ext2"])
print(l)
l.insert(9,0)
print(l)

l1 = [1,2,3]
l2 = [1,0,0]
print(l1+l2)
print(l1)
l1.extend(l2)
print(l1)