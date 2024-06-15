lst=eval(input())
once=[]
for i in lst:
    if lst.count(i)==1:
        once.append(i)
if once==[]:
    print("False")
else:
    once.sort(reverse=False)
    new=",".join(str(i) for i in once)
    print(new)
