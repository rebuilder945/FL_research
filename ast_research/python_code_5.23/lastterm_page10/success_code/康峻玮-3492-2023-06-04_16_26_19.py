x=input()
for i in x:
    if x.count(i)==1:
        print(i)
        break
    if len(x)==0:
        print("None")
