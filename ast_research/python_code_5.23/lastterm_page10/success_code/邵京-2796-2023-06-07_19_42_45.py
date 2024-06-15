str=input()
digit=[]
for i in str:
    if i.isdigit():
        digit.append(i)
    elif i.alpha():
        digit.append(',')
longestdigit=[]
a=0
for i in digit():
    if i==',':
        for x in range(a+1,i):
            digitstr=digit[a]
            digitstr+=digit[x]
            a=i
            longestdigit.append(digitstr)
print(longestdigit)

