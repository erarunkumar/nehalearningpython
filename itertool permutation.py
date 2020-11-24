"""s=input("enter string and range").split()
a=int(s[1])
string=s[0]
from itertools import permutations
p=list(permutations(sorted(string),a))
for x in p:
    for y in x:
         print(y,end="")
    print()"""

#easy program on itertools
# itertools permutation
from itertools import permutations
s,n= input("enter string,range").split()
print(*[' '.join(i)for i in permutations(sorted(s),int(n))],sep ='\n')
print()

# itertools combinations
from itertools import combinations
s , n  = input("enter string ,range").split()
for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print(''.join(j))

# itertools combinations_with_replacement
from itertools import combinations_with_replacement
s, k = input("enter string ,range").split()
for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))





