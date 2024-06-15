lst=list(input().split(" "))
mun=list(input().split(" "))
a=lst[int(mun[0])]
b=lst[int(mun[1])]
lst[int(mun[0])]=b
lst[int(mun[1])]=a
print(lst)
