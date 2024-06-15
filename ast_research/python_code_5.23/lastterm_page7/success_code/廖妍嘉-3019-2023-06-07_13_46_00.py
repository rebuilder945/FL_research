n=input().split()
ls=n[1:]
ls2=[]
sum=0
for i in ls:
    a=eval(i)
    ls2.append("%.2f"%(a))
    sum+=a
ls2.sort()
ave="%.2f"%(sum/len(ls2))
ls2.append(ave)

b=' '.join(str(i) for i in ls2)
print(n[0],b)


