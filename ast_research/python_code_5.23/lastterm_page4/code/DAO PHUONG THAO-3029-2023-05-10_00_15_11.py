names=input().split(",")#输入逗号分割的字符串作为列表
scores=eval(input())#输入列表，带方括号
r=[]
for i in range(len(names)):#位置遍历，使用了位置区间range
r.append([names[i],scores[i]])#把两个对应位置的元素合并成一个列表，作为一个元素追加到结果列表
print(r)
