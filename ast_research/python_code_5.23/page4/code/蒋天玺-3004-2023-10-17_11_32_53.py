def sushu(y):
    x=[]
    for i in y:
        if i>=2:
            for j in range(2,i,1):
                if i%j==0:
                    break
            else:
                x.append(i)
    print(x)
sums=eval(input())
sushu(sums)
————————————————
版权声明：本文为CSDN博主「Ta似白月中来」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ty520183/article/details/130836571

