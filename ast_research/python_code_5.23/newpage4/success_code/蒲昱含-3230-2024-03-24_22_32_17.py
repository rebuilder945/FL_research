list=[]
n=int(input())
for i in range(n):
    x=int(input(""%(i+1)))
list.append(x)
list.sort(reverse=True)
print(list)
