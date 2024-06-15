lt=[1,2]
n=int(input())
ii=[]
for i in range(4):
    i=sum(lt[-2:])
    lt.append(i)
#print(lt)
t=0
for i in range(n):
    fenzi=lt[i]
    fenmu=lt[i+1]
    nn=fenmu/fenzi
    #print(nn,end="")#这里忘记缩进就只打印最后一个数字
    t=t+nn
print("{:.4f}".format(t))
