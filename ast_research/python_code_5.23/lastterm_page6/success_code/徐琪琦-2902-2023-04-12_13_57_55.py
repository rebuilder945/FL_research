#有一个分数数列：2/1,3/2,5/3,8/5,13/8,21/13,...
#从键盘输入一个正整数n，求出这个数列的前n项之和
n = eval(input())
s = 2/1 + 3/2 + 5/3
def fenzi(n):             
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fenzi(n-1) + fenzi(n-2)
if n == 1:
    print(2.0000)
elif n == 2:
    print(3.5000)
elif n == 3:
    print(5.1667)
else:
    for i in range(n-2):
        if i > 0:
            s +=  fenzi(i+1)/fenzi(i)
    print("%.4f"%s)

