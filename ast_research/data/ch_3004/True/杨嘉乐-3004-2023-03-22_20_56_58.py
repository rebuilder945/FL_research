l=eval(input())
ll=[]
for x in l:
    a=0
    for i in range(x-2):
        if x%(i+2)==0:
            a=1
            break
    if a==0:
        ll.append(x)
if 0 in ll:
    ll.remove(0)
if 1 in ll: 
    ll.remove(1)    
print(ll)
