import sys
num=eval(input())
num.sort(reverse=True)
if num[0]==0:
    print(0)
    sys.exit(0)
for x in num:
    print(x,end="")

