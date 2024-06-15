#输出n以内的所有的回文素数。若n输入不合法（为小数或负数），则输出提示“illegal input”
#先找到回文数 再判断素数
hws = []
n = eval(input())
if type(n) == int:
    for num in range(2,n+1):
        if str(num) == str(num)[::-1]:	#str[::-1]表示字符串反转
            hws.append(num)
    for i in hws:
        for j in range(2,i):
            if int(i)%j==0:
                hws.remove(i)
    for x in hws:
        print(x,end=" ")
else:
    print("illegal input")

