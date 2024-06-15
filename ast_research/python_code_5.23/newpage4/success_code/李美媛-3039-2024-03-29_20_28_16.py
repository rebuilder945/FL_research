list=eval(input())
maxnum=max(list)
minnum=min(list)
list=[x for x in list if x != maxnum and x != minnum]
print(list)
