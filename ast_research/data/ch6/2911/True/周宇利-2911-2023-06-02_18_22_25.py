list1=list(input())
for i in range(len(list1)):
    list1[i]=(eval(list1[i])+5)%10
list1[0],list1[-1],list1[1],list1[-2]=list1[-1],list1[0],list1[-2],list1[1]
for k in list1:
    print(k,end='')
