dic={}
ls=input().split()
dic['name']=ls[0]
dic['english']=ls[1]
dic['python']=ls[2]
dic['math']=ls[-1]
del ls[0]
dic['avg']=(sum(ls)/len(ls))
print("%s,%.2f,%.2f,%.2f"%(dic['name'],ls[0],ls[1],ls[2],dic['avg']))
