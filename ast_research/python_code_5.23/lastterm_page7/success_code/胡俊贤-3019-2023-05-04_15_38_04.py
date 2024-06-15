dic={}
ls1=input().split()
dic['name']=ls1[0]
dic['english']=ls1[1]
dic['python']=ls1[2]
dic['math']=ls1[-1]
del ls1[0]
ls=map(int,ls1)
dic['avg']=(ls[0]+ls[1]+ls[2]/3)
print("%s,%.2f,%.2f,%.2f"%(dic['name'],ls[0],ls[1],ls[2],dic['avg']))
