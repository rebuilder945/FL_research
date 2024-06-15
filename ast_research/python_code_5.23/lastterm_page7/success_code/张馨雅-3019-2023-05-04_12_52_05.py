inf=input().split(' ')
dic={}
dic['name']=inf[0]
dic['english']=inf[1]
dic['python']=inf[2]
dic['math']=inf[3]
g=[]
g.append(int(dic['english']))
g.append(int(dic['python']))
g.append(int(dic['math']))
g.sort(reverse=True)
avg=sum(g)/3
dic['avg']=avg
print('%s %.2f %.2f %.2f %.2f'%((dic['name']),(g[0]),(g[1]),(g[2]),(dic['avg'])))
