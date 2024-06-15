def sxhs(x):
    a=x
    t = 0
    while x!=0:
        t+=(x%10)**3
        x=x//10
    if a==t:
        print(a)
        return True
f = 0
x = eval(input())
for i in range(2,x+1):
    if sxhs(i):
        flag = 1
if flag == 0:
    print("none")
