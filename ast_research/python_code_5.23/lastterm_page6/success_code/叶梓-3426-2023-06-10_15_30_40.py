#x=eval(input())
#if x<20:
#    d=6*(x**2)+1
#if x>=40:
#    d=100/(x+1)
#else:
#    d=(3*x - 60)**(1/2)
#print(".2f"%d)

def cal(n1): # 定义函数
    if n1 < 20:
        n2 = 6 * n1 ** 2 + 1
    elif 20 <= n1 < 40:
        n2 = (3 * n1 - 60) ** 0.5
    else:
        n2 = 100 / (n1 + 1)
    return n2
num1 = eval(input())
num2 = cal(num1)
print("%.2f" % num2)
