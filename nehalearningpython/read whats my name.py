def print_full_name(a, b):
    print(("Hello %s %s! You just delved into python.") % (first_name ,last_name))

if __name__ == '__main__':
    first_name = str(input("enter first name"))
    last_name = str(input("enter last name"))
    print_full_name(first_name, last_name)

a= int(input("first name"))
b= int(input("second name"))
print(a ,b)
print(("Hello  %d ,%d! You just delved into python.")% (a,b))