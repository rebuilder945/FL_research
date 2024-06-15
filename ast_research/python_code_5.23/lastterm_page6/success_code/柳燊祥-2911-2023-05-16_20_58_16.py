lst1=list(input())
for i in range(len(lst1)):
    lst[i]=(eval(lst1[i])+5)%10
lst[0],lst[-1],lst[1],lst[-2]=lst[-1],lst[0],lst[-2],lst[1]
for i in lst1:
    print(i,end='')
