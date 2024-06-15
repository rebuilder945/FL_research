a=0
list1=eval(input())
for i in range(0,len(list1)):
    a=a+int(list1[i])
    b=a/len(list1)
    if a%1==0:
        print(int(b))
    else:
        print("%.2f"%b)
