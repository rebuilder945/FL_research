old=input()
new=[]
for i in range(len(old)):
    new.append(int(old[i]))
for j in range(len(new)):
    new[j]=(new[j]+5)%10
new.reverse()
for k in range (len(new)):
    print(new[k],end='')
