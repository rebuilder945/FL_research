#列表里只包括小写字母，输出时以a-z的顺序输出
strlist = eval(input())
Count = {}
for str in strlist:
    for char in str:
        Count[char] = Count.get(char,0) + 1
for i in sorted(Count.key()):
    print("%s,%d"%(i,Count(i)))

