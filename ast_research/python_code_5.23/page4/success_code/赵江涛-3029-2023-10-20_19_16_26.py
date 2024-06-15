from itertools import combinations
from pydoc import stripid

name = strip(input())
grade = eval(input())
comb = []
for i in range(len(grade)):
    ls = []
    ls.append(name[i])
    ls.append(grade[i])
    comb.append(ls)
print(comb)

