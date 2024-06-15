lst=eval(input())
lst1=[]
for x in lst[::-1]:
    if x not in lst1:
        lst1.append(x)
lst2=lst1[::-1]
print(lst2)



#python如何删除列表中重复元素并且保留最后一个重复值 
# 1往后切 看是不是出现了一次 不是 加入 
#copy的注意删除全部重复的，删除一个重复的保留一个的区别  想清楚对哪个进行操作
#2in not in 倒过来reverse 或者 [::-1]因为是保留最后一个重复的元素 reverse两遍

