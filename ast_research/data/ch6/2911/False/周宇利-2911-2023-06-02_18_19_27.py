list1=list(input())
for i in range(len(list1)):
    list1[i]=(eval(list1[i])+5)%10
    for j in range(len(list1)):
        list1[j]=list1[-j-1]
        for k in list1:
            print(k,end='')
