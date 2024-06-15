s = ''.join(eval(input()))
for x in "abcdefghijklmnoppqrstuvwxyz":
    if x in s:
        num = s.count(x)
        tmp = x+','+str(num)
        print(tmp)
