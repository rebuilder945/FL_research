s = 0
n = 0
flag = 1
while(flag):
    t = input()
    if (t != "#"):
        n += 1
        s += int(t)
    else:
        flag = 0
print(n,s)      #print(n,end=" ")
                #print(s)
