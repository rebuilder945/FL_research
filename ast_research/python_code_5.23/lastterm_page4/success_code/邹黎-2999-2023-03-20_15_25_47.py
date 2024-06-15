list2=list(input().split(" "))
list0=list(input().split(" "))
a=list0[0]
b=list0[1]
achu=list2[a]
bchu=list2[b]
list2[a]=bchu
list2[b]=achu
print(list2)
