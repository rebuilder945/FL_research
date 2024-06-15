line=input()
a=1
for i in line:
    if line.count(i)==1:
        print(i)
        a=a+1
        break
if a==1:
    print("None")   

