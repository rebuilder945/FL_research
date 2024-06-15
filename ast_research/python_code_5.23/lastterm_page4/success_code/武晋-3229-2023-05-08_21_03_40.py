lst=eval(input())
b=[]
for i in lst:
    if lst.count(i) == 1:
        b.append(i)
    else:
        continue
b=b.sort(reverse=True)
if len(b)==0:
    print("False")
else:
    print(b)


    



