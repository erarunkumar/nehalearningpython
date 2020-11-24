list1 = (1, 2,3,4,5,6)
list2=('neha','manisha','seema','rajni','ravi')
zipped = list(zip(list1, list2))

print(zipped ,'\n')


unzipped = list(zip(*zipped))
print(unzipped)
print()

for (l1,l2) in zip(list1,list2):
    print(f'{l1,l2.strip()}={l1,l2.strip()}')
    print()
    print(l1 ,l2)


print()



def fruits():
    obj =['mango','banana','litchi']
    quantity = (4,6,7)
    prices = (45.8,56.3,89.0)
    santances = []
    for object , quant,price in zip(obj,quantity,prices):
        print(object , quant,price)
fruits()

def sentance():
    list1 = ['A', 'app', 'i','a', 'd', 'ke', 'th', 'doc', 'awa']
    list2 = ['y', 'tor', 'e', 'eps', 'ay', None,'n', 'le', 'n']
    a = list2.remove(None)
    list2.insert(5, "")
    list3 = [str(x[0]) + x[1] for x in zip(list1, list2[::-1])]
    print (' '.join(list3))
sentance()



