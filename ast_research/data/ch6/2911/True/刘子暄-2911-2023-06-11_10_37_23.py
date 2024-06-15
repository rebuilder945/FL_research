lst1=list(input())
for i in range(len(lst1)):
    lst1[i]=(eval(lst1[i])+5)%10
lst1.reverse()
for i in lst1:
    print(i,end='')
