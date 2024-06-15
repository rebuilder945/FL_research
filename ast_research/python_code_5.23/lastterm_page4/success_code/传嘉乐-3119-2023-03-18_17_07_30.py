l=eval(input())
ll=[]
for x in l:
    if l.count(x)>1:
        ll.remove(x)
print(ll)
