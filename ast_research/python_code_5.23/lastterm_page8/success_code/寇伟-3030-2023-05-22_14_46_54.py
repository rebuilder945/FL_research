f=open("score.txt","r")
a=f.read().split("\n")
#直接按行读取
inf=[]
for x in a:
    inf.append(x.split(","))
#以逗号分隔添加到inf列表中
inf.sort(key=lambda x:-(int(x[2])+int(x[3])+int(x[4])))
#inf列表排序
print(inf)
f.close()

f=open("sorted.txt","w")
for x in inf:
    f.write("{},{},{},{},{}".format(x[1],x[0],x[2],x[3],x[4]))
    f.write("\n")
#个人十分推荐手动打出"\n"
