num=input()
li=[]
for i in range(len(num)):
    li.append(int(num[i]))
    li[i]=(li[i]+5)%10
li.reverse()
for x in li:
    print(x,end='')

