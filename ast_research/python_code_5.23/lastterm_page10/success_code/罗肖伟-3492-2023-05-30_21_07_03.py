s=list(input())
for i in s:
    x=s.count(i)
    if x==1:
        print(i)
        break
else:
    print("None")
