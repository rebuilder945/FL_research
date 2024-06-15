nums=eval(input())
n,m=eval(input())
list1=list(nums)
if n>len(list1):
    print("error")
else:
    a=list1[n]
    while m>0:
        list1.append(int(a))
        m-=1
    print(list1)
