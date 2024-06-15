l=eval(input())
l2=[]
for i in l:
    if l.count(i)==1:
        l2.append(i)
        l2.sort(reverse=False)
        print(l2)
    else:
        print("False")
