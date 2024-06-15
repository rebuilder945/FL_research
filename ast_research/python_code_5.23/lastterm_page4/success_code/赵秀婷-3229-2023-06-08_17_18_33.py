# 在列表中找出只出现一次的元素，并排序输出
lst=eval(input())
lst.sort()
for i in lst[:]:
    while lst.count(i)>1:
        lst.remove(i)
if lst==[]:
    print("False")
else:
    c=list(map(str,lst))
    print(",".join(c))
