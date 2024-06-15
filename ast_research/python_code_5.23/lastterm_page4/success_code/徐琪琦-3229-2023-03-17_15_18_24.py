#输入一个自然数列表，找出只出现一次的元素，并升序输出。如果没有只出现一次的元素，则输出False。(没说的话，自己也要考虑到这种情况！)
list1 = eval(input())
list2 = []
for i in list1:
    if list1.count(i) == 1:
            list2.append(str(i))
if len(list2) != 0:
    list2.sort()
    print(",".join(list2))             #join函数的用法
else:
    print("False")
    


