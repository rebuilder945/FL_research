a=input()
list1=a.split()
n,m=eval(input())
list1[n],list1[m]=list1[m],list[n]
if n<=len(list1) and m<=len(list1):
    print(list1)
