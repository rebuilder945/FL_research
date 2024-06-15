#给定一个字符串，取出第一个没有重复的字符，如果输入为空则输出"None"。
demo = input()
lst = []
if len(demo) == 0:
    print("None")
else:
    for i in demo:
        if demo.count(i) == 1:
            lst.append(i)
            break
        else:
            pass
print(lst)



