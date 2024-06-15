word=str(input())
lis=word.split()
dic={"num":0}
for i in range(0,len(lis)):
    for j in lis[i]:
        dic["num"]=dic["num"]+1
print("%d,%.2f"%(len(lis),dic["num"]/(len(lis))))
