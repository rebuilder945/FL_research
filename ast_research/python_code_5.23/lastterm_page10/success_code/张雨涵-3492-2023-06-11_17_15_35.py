a=list(input())
c=[]
for i in a:
    b=a.count(i)
    if b == 1:
        print(i)
        break
else:
    print("None")
