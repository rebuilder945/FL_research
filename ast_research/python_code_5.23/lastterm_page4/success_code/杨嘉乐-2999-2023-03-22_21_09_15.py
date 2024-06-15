ll=input().split(" ")
a,b=map(int,input().split(" "))
temp=ll[a]
ll[a]=ll[b]
ll[b]=temp
print(ll)
