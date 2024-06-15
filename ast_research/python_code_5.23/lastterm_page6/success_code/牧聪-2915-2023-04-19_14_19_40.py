num=int(input())
nums=[]
for n in range(num):
    a=str(n)
    lst=[]
    for x in a:
        t=int(x)**3
        lst.append(t)
    if sum(lst)==int(a):
        nums.appned(sum(lst))
        print(sum(lst))
if nums==[]:
    print("none")
    







