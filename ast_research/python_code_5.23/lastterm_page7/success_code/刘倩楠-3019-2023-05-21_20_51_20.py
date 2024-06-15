i = 0
scores=[]
#创建scores列表，储存学生信息
while i < 3:
    u,v,x,y = input().split(" ")
    di=(("name",u),("english",int(v)),("python",int(x)),("math",int(y)))    
    #int类型装换，方便后续使用round函数
    di = dict(di)
    #元组类型转换字典方便后续使用字典索引，添加['avg']
    scores.append(di)
    i=i+1
for i in scores:    #列表遍历，列表中的每个元素是字典
    i["avg"]=round((i["english"]+i["python"]+i["math"])/3,2)
scores.sort(key=lambda x:x['avg'],reverse=True) 
#lambda 字典嵌套列表类排序
#确定排序标准：每个字典x中的平均成绩，降序
#上述line 14，也可改为scores.sort(key=lambda x:-x['avg'])
#通过比较正数的相反数得到目的
print(scores)
#输出打印
