a=eval(input())
lst1=[]
lst1.append(a)
for i in range(len(lst1)):
    lst1[i]=(eval(lst1[i])+5)%10
    lst1[i]=lst1[i-1]
for i in lst1:
    print(i,end="")
