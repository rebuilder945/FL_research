nums=eval(input())
n,m=eval(input())
c=len(nums)
if n<c and m<c:
    del nums[n:m]
    print(nums)
if n>c or m>c:
    print("error")
