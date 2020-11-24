"""n = int(input("enter the no"))
integer_list = map(int, input("enter value").split())
t = tuple(integer_list)
print (hash(t)) """

student1 = (234 ,'6/7' ,'arun')
student2 =('neha' , 'bca' , 'mca', 2014)

students = [student1, student2]
print(students)

person1 = ("nancy pents" , 43 , 'pizza')
person2 =("joe shirt", 34,'pasta')
person3 = ("asji bangel", 33,'panner')
people = [person1 ,person3,person2]
"""(name ,age,favfood) = person
print( "name = " ,name)
print( "age =", age)
print("favfood =" ,favfood)"""

for name ,age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()
