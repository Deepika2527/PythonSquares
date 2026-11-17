txt = "123P456#46u"
print(txt)
print(len(txt))
print("Ends,", txt.endswith("u"))
print("Ends,", txt.endswith("U"))
print("Starts, ", txt.startswith("1"))
print("Starts, ", txt.startswith('A'))
print("isAlpa: ", txt.isalpha())
print( "ag".isalpha())

print("------------------------------------------------------------")
sen = "welcome^AIT"
print(sen.isalpha())
sen1 = "hello world"
print(sen1.isalpha())

print("----------------------Alphanumeric---------------------------------------")
pswd = "Welcome12344"

print(pswd.isalnum())
print('Welcome 123'.isalnum())
print('Welcome&123'.isalnum())

print('------------------0-9 validates and returns true  decimal values-------------------')
print('1234'.isdecimal())
print('-1234'.isdecimal())
print('Ⅹ'.isdecimal())
print('½'.isdecimal())
print('45.6'.isdecimal())


print("--------isNumeric workkd with roman,super,fraction but not -ve and float-------")
print('1234'.isnumeric())
print('-1234'.isnumeric())
print('Ⅹ'.isnumeric())
print('½'.isnumeric())
print('⁰'.isnumeric())
print('34.6'.isnumeric())


print("-----Isdigit- Only for no's and super------")
print('1234'.isdigit())
print('-1234'.isdigit())
print('Ⅹ'.isdigit())
print('½'.isdigit())
print('⁰'.isdigit())
print('34.6'.isdigit())

