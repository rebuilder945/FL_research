a,b,c,d=input().split()
ls=[int(b),int(c),int(d)]
max_=max(ls)
min_=min(ls)
for i in ls:
    if i!=max_ and i!=min_:
        e=i
    elif max_==min_ and max_!=0:
        e=max_
    elif max_==min_==0 :
        e=0
avg=(int(b)+int(c)+int(d))/3
print(a,'{:.2f}'.format(float(max_)),'{:.2f}'.format(float(e)),'{:.2f}'.format(float(min_)),'{:.2f}'.format(float(avg)))

