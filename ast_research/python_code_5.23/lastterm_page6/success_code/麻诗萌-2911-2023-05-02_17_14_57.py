# 定义函数stu(x)，判断数字x是否为素数
def stu(x):
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True
# 定义函数main(n),先遍历找到符合p+q=n且p<=q的数，再判断p,q是否为素数，找到后使用break终止循环可确保只输出最小的p
def main(n):
    for p in range(2,n):
        if p<=n-p:
            q=n-p
            if stu(p):
                if stu(q):
                    print(str(n),"=",str(p),"+",str(q))
                    break
# 输入N
N=eval(input())
# 调用main函数
main(N)
