from collections import namedtuple
n, Score = int(input("enter value")) , namedtuple('Score',input("enter score").split())
scores = [Score(*input("enter").split()).MARKS for i in range(n)]
print("%.2f"% (sum(map(int,scores))/n))




///
#word worder program
from collections import Counter
n= int(input())
l=list()
for _ in range(n):
    l.append(input())
x= Counter(l)
#print(x)
print(len(x))
print(*x.values())///