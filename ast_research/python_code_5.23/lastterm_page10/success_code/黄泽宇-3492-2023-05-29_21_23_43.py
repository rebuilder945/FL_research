x=input()
a=[]
for i in range(len(x)):
    a.append(x[i])
for s in range(len(a)):
    if a.count(a[s]) == 1:
        print(a[s])
        break
    else:
        print("None")
