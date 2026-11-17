str = "hello all..Hope You are Doing well??"
print(str)
print(len(str))
print("Upper:",str.upper())
print(str)
# Because strings are immutable. These methods return a new string; they don't modify the original string.
print("Lower:",str.lower())
print("Capitalise",str.capitalize())
print("SwapCase:",str.swapcase())
print("CaeFold:",str.casefold())
print("Title:",str.title())

print("---------------------")
txt = "Text"
print(txt)
print(id(txt))
txt = txt.upper()
print(txt)
print(id(txt))
# But here id are diffe

a = "straße"
b = "STRASSE"

print(a.casefold() == b.casefold())
print(a.lower() == a.lower())