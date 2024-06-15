n = 0
s = 0
flag = True
while(flag):
    num = input()
    if num!="#":
        n += 1
        s += int(num)
    else:
        flag = False
print(n,s)
