import textwrap

def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width):
        s += string[c:c+max_width] + "\n"
    return s

if __name__ == '__main__':
    string, max_width = input("enter any alphabeticals"), int(input("enter any no "))
    result = wrap(string, max_width)
    print(result)

s=""
string =input("enter any alphabeticals")
max_width = int(input("enter any no "))
for c in range(0, len(string), max_width):
    s += string[c:c + max_width] + "\n"
print(s)