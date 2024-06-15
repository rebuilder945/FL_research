import copy
ll=eval(input())
lll=copy.deepcopy(ll)
for i in lll:
    if ll.count(i)>=2:
        for pp in range(ll.count(i)-1):
            ll.remove(i)
print(ll)
