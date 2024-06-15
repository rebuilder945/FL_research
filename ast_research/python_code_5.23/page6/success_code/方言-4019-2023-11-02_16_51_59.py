ps=input()
li=[]
sum=0
for i in ps:
    li.append(int(i))
    li[-1]=(li[-1]+5)%10
for i in range(len(ps)):
    sum=sum*10+(li.pop())
print(sum)
