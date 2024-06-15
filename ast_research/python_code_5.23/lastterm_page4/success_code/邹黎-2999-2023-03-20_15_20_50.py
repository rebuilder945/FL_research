list=list(input().split(" "))
a,b=eval(input())
achu=list[a]
bchu=list[b]
list[a]=bchu
list[b]=achu
print(list)
