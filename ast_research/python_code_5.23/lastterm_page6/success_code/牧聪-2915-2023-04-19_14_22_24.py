num=int(input())
nums=[]
print(num)
for n in range(100,num):
    a=str(n)
    lst=[]
    for x in a:
        t=int(x)**3
        lst.append(t)
    if sum(lst)==int(a):
        nums.append(sum(lst))
        print(sum(lst))
if nums==[]:
    print("none")
    







