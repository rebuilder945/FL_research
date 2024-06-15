# 存储学生Zhang成绩的字典结构如下：
# stu={"name":"Zhang","english":80,"python":90,"math":100}
# 1）请使用上述结构输入学生的name及english、python和math三门课的成绩并存储到字典stu中(不考虑空数据的情况)；
# 2）计算该同学的平均成绩，同时在字典中添加关键字"avg"用来表示平均成绩；
# 3）由高到低排序该学生的各科成绩；
# 4）输出该学生的姓名，各科成绩（保留两位小数）和平均成绩（保留两位小数）。
s = input().split()
dic = {}
dic["name"] = s[0]
dic["english"] =s[1]
dic["python"] = s[2]
dic["math"] = s[3]
dic["avg"] = (int(dic["english"]+dic["python"]+dic["math"]))/3
lst = []
for i in dic:
    if type(eval(dic[i])) == type(1):
       lst.append(dic[i]) 
lst.sort()
print("{}{:.2f}{:.2f}{:.2f}{:.2f}".format(dic["name"],lst[0],lst[1],lst[2],dic["avg"]))
