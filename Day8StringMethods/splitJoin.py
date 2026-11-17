st = "Hello, Hi, all, - To you-all"
print(st.split(','))
print(st.split(" "))
print(st.split("^"))
print(st.split(",",2))

print("------------------------")
text = "apple,banana,mango,orange"

print(text.rsplit(",", 2))


print("-----------------------------------")
words = ["Hello", "Python", "World"]

result = " ".join(words)

print(result)
print(" ".join(words))
print("-".join(words))
print(",".join(words))
print("".join(words))