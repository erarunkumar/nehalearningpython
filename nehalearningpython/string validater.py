s = input("enter any char")
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print (any(method(c) for c in s))


print()
print()

print ('abcD'.isalpha())
print ('1234'.isdigit())

print ('123edsd'.isdigit())
