from collections import OrderedDict
d=OrderedDict()
for i in range(int(input("enter range"))):
    item,space,quantity=input("enter fruits and quantity ").rpartition(' ')
    d[item]=d.get(item,0) + int (quantity)
for item,quantity in d.items():
    print(item,quantity)