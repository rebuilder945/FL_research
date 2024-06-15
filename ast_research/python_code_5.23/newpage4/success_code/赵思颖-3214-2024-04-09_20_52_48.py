# List=eval(input())
# aa=List.remove(0)
# # List.remove(0)
# print(List.remove(0).extend(aa))

from itertools import count


lists=eval(input())
lists2=[]
for i in  lists:
    if i!=0:
        lists2.append(i)
n=lists.count(0)
for i in range(n):
    lists2.append(0)
print(lists2)
