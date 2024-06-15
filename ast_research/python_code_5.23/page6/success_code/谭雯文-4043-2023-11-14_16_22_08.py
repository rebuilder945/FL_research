a="".join(eval(input()))
# a=input().split(",")
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in a:
        num=a.count(i)
        tem=i+","+str(num)
        print(tem)
