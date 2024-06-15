alist=eval(input())
a=sum(alist)/len(alist)
if sum(alist)%len(alist)==0:
    print(int(a))
else:
    print(round(a,2))

