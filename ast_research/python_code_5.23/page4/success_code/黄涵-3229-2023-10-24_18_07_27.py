#输入一个自然数列表，找出只出现一次的元素，并升序输出。如果没有只出现一次的元素，则输出False
a = eval(input())
for x in a :
    if a.count(x)>1 :
        for i in range(a.count(x)) :
            a.remove(x)
if len(a)>0 :
    a.sort()
    print(','.join(str(i) for i in a))
else :
    print(False)
