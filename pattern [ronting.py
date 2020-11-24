string = input("enter any word")
length = len(string)
for row in range(length):
    for col in range(row):
        print(string[col], end ="")
    print()