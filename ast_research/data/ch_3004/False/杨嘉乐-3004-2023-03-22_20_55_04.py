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
print(ll)
