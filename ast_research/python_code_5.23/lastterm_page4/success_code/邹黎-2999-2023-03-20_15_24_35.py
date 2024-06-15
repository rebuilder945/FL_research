list=list(input().split(" "))
list0=list(input().split(" "))
a=list[0]
b=list[1]
achu=list[a]
bchu=list[b]
list[a]=bchu
list[b]=achu
print(list)
