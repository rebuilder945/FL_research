num=eval(input())
r=[]
for n in num:
    if num.count(n)==1:
        r.append(n)
r.sort()
if r:
    print(",".join(str(i) for i in (r)))
else:
    print("False")
          
