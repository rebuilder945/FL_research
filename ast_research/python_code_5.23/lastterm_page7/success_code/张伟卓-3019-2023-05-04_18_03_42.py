a,b,c,d=input().split()
ls=[b,c,d]
max_=max(ls)
min_=min(ls)
for i in ls:
    if i!=max_ and i!=min_:
        e=i
avg=(int(b)+int(c)+int(d))/3
print(a,'{:.2f}'.format(float(max_)),'{:.2f}'.format(float(e)),'{:.2f}'.format(float(min_)),'{:.2f}'.format(float(avg)))
