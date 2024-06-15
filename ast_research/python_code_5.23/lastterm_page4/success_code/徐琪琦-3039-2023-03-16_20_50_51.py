#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个。
list1 = eval(input())
maxlist1 = max(list1)
minlist1 = min(list1)
while max(list1) == maxlist1:
    list1.remove(maxlist1)
if len(list1) > 0:
    while min(list1) == minlist1:          #没有上一行，直接while min(list1) == minlist1:     list1.remove(minlist1)为什么不行？当list1只有一个元素并且去掉了之后，min(list1)就没有意义了啊
        list1.remove(minlist1)
print(list1)

