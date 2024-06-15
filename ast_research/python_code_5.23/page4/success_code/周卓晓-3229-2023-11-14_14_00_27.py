a = eval(input())
ls = []
flag = 0
for i in a:
    if a.count(i)==1:
        ls.append(str(i))
        ls.sort()
        flag=1
if flag == 1:
    print(",".join(ls))
elif flag ==0:
    print("False")


    
        



