s=input()
flag=False
for i in s:
    if s.count(i)==1:
        print(i)
        flag=True
        break
if flag  == False:
    print("None")


