
l = eval(input())
lst = []
for i in l:
     if l.count(i) == 1:
            lst.append(i)
if lst == []:
    print("False")
else:   
    lst.sort()
    print(*lst,sep=',')

