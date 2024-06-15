lst=eval(input())
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in lst:
        num=lst.count(x)
        ly=x+","+str(num)
        print(ly)
