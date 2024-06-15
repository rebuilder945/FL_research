s=input()
b=[]
for x in range(1,len(s)):
    for i in range(len(s)-x+1):
        b.append(s[i:i+x])
b.append(s)
b.reverse()
for i in b:
    if i.isdigit():
        print(i)
        break
else:
    print("No digits")

    
