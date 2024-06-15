#给定一个字符串，取出第一个没有重复的字符，如果输入为空则输出"None"。
s=input()
if s:
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print("None")
else:
    print("None")

