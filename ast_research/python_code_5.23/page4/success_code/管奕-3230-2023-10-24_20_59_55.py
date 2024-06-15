list=eval(input())
list1=list.sort(reverse=False)
n=len(list)
a=[list1[x]*10**(n-int(index(x))) for x in list1]
b=sum(a)
print(b)
