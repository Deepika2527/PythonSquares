ex = "hello$"
ex1 = 'Hello World'
ex2 = '''hello.how are you'''
print(ex)
print(ex1)
print(ex2)
print(type(ex), type(ex1), type(ex2))
print(ex[0])
print(len(ex))
# ex[0] = ex[1]
print("Postive Indexing...", ex[1])
print("negative Indexing...",  ex[-1])
print("Jk"+"lk")
print("Hi"*2)
print("Hi" == "hi")
print("Hello" in "Hello")

print("Hello" is "Hello")
a = "Hello"
b= "Hello"

print(a is b)
a1 = [1,2]
b1= [1,2]
print(a1 is b1)
print(a1 == b1)
s = "Apple"  
s1 = "Apple"  
print(s == s1)
print(s < s1)
print(s > s1)


str1 = "Hello Catty How are you dng??123"
print("-------------------")
print(len(str1))
print(str1[1:4])
print(str1[2])
print(str1[4:])
print(str1[-1])
print(str1[-4:-1])
print(str1[-8])
print(str1[-8:])
# print(str1[-5:-7]) 
# empty because in negative slicing we need use bigVale:smallvalue
print(str1[33:]) 
# empty
print(str1[-34:]) 
# It will print everything as egative indexing and also it will retreive everything from Right to left
# print(str1[33])
# out if range
word = "Python"
print("------------------------------------")
for word in "ho":
    print(word)
print("--------------------------------------")
for n in range(1,10):
    print(n)
    print("***")
char = 'python'
for ch in range(len(char)):
    print(ch)
string1 = "Hello"
for k,v in enumerate(string1):
    print(k, ":", v)

