s=list(input())
x=[]
for i in range(len(s)+1):
    if s[i].isdigit() and s[i+1].isdigit():
        x.append(s[i])
    elif s[i].isdigit() and s[i+1].isdigit()!=True:
        x.append(s[i])
        x.append(",")

x.sort(reverse=True)
print(x[-1])
