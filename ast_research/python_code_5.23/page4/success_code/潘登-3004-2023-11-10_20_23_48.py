a=input()
s=[]
for x in a :
    if x>2:
        for i in range(x):
            if x%i != 0:
                s.append(x)
                break
print(s)
