s = {}
while True:
    n = input()
    if n == "q":
        break

    if n in s:
        s[n]+=1
    else:
        s[n]=1
    # print(s)
max1 = 0
max2 = ''
for x in s:
    if s[x]>max1:
        max1 = s[x]
        max2 = x
print(max2,max1)
