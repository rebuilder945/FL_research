lst=eval(input())
n,m=eval(input())
if n>m or n<0 or m>len(lst):
    print("error")
for i in range(m-n):
    del lst[n]
print(lst)
