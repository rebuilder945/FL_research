#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个。
list1 = eval(input())
maxlist1 = max(list1)
maxnum = list1.count(maxlist1)   #maxlist1不要加引号！！！
minlist1 = min(list1)
minnum = list1.count(minlist1)
i = 1
x = 1
while i < maxnum + 1:
    list1.remove(maxlist1)
    i += 1
while x < minnum + 1:         #有考虑到当list1只有一个元素并且去掉了之后，min(list1)就没有意义了啊.还有不能再用i了！
    list1.remove(minlist1)
    x += 1
print(list1)
