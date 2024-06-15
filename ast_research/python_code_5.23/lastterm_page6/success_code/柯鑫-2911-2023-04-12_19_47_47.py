list1=list(input())
a=len(list1)
for i in range(a):
    list1[i]=(eval(list1[i])+5)%10
    list1[0],list1[-1],list1[1],list1[-2]=list1[-1],list1[0],list1[-2],list1[1]
for i in list1:
    print(i)

