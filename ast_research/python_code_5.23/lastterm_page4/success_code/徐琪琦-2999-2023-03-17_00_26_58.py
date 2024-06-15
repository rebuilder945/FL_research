#输入一个由字符串构成的列表和两个整数n和m（n和m在输入列表的下标范围以内），交换其中两个元素的值，打印输出交换后的列表。li
list1 = input().split()   #如果用split(""), ""里面别忘了敲一个空格啊
indexlist= input().split()   #如果里面是列表，外面不可以加eval了，eval里面必须是string
n = indexlist[0]
m = indexlist[1]              #注意你的操作是在原列表之外还是改变了原列表的值
if int(n) > 0 and int(m) > 0:            
    if int(n) < int(m):               #注意操作之后列表中元素的序号变了啊
        a = list1.pop(int(n))
        b = list1.pop(int(m)-1)             
        list1.insert(int(n),b)
        list1.insert(int(m),a)
        print(list1)
    elif int(n) == int(m):
        print(list1)
    else:
        a = list1.pop(int(n))
        b = list1.pop(int(m))        
        list1.insert(int(m),a)
        list1.insert(int(n),b)
        print(list1)
elif int(n) < 0 and int(m) > 0:
    a = list1.pop(int(n))
    b = list1.pop(int(m)-1)             
    list1.insert(int(n)+1,b)
    list1.insert(int(m),a)
    print(list1)
elif int(n) > 0 and int(m) < 0:
    a = list1.pop(int(n)-1)
    b = list1.pop(int(m))             
    list1.insert(int(n),b)
    list1.insert(int(m)+1,a)
    print(list1)
else:                                       #把负的序号变成正的，好研究。
    if len(list1)-int(n) < len(list1)-int(m):               
        a = list1.pop(len(list1)-int(n))
        b = list1.pop(len(list1)-int(m)-1)             
        list1.insert(len(list1)-int(n),b)
        list1.insert(len(list1)-int(m),a)
        print(list1)
    elif len(list1)-int(n) == len(list1)-int(m):
        print(list1)
    else:
        a = list1.pop(len(list1)-int(n))
        b = list1.pop(len(list1)-int(m))        
        list1.insert(len(list1)-int(m),a)
        list1.insert(len(list1)-int(n),b)
        print(list1)
