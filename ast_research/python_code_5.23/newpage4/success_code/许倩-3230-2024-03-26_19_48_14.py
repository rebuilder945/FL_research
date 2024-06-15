# 2023-2024（2）基础题库练习：第4章
# 第一题
lst=eval(input())
lst.sort(reverse=True)
sum=''
for i in range(len(lst)):
    sum+=str(lst[i])
print(int(sum))


