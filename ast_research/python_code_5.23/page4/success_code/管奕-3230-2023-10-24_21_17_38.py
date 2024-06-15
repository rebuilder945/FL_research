list=eval(input())
list1=list.sort(reverse=True)
n=len(list)
a=[int(list1[x])*10**(n-int(list1[x])) for x in len(list1)]
b=sum(a)
print(b)
