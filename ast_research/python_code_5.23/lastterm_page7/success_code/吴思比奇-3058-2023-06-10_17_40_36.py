str_list=[]
#input标准化输出
while True:
    dummy=input()
    if dummy != "q":
        str_list.append(dummy)
    else:
        pass
        break
str_dict={}
for x in str_list:
    str_dict[str(x)]=str_list.count(x)
finlist=[]
value_list=[]
#创建列表反馈次数
for k,v in str_dict.items():
    finlist.append([k,int(v)])
    value_list.append(int(v))
for x in finlist:
    if x[1] == max(value_list):
        print(x[0],x[1])





