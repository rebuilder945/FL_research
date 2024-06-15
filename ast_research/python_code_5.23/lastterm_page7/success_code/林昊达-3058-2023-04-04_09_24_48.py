# 【问题描述】

# 编写一个程序，从键盘读取未指定个数的字符串，一行一个，以字符串"q"为输入结束标志（"q"不列入统计范围）。

# 使用字典找出其中出现次数最多的字符串，打印该字符串及其出现次数。 

# 注意：本题的测试用例中将保证只有一个字符串出现次数最多，且至少有一条数

# 【样例输入】

# abc

# abc

# bcd

# xxx

# q


# 【样例输出】

# abc 2



# 【样例说明】

# 输入为不定行，以"q"结束，q是结束标志，不属于需要统计的字符串。

# 输出为一行，出现次数最多的字符串（只有一个）及其出现次数，由空格隔开。


dic={}
item=input()
while item!='q':
    if item not in dic:
        dic[item]=1
    else:
        dic[item]+=1
    item=input()
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
print(ls[0][0],ls[0][1])

