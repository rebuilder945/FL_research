list=eval(input())
list1=list.sort(reverse=True)
n=len(list)
a=[list1[x]*10**(n-x) for x in len(list)]
b=sum(a)
print(b)
