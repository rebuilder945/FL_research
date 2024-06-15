a=eval(input())
if type(a)!=int:
    print("illegal input")
else:
    for i in range(a):
        flag=0
        flag1=0
        for j in range(i):
            if i%j==0:
                flag=1
        if flag==0:
            if i>10:
                char=str(i)
                for m in range(len(char)):
                    if char[m]!=char[len(char)-1-m]:
                        flag1=1
                        break
                if flag1==0:
                    print(i,end='')
