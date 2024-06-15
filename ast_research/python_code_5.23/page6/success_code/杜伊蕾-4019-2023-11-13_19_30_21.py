'''def  main():
        a=int(input())
        calculate_sum(a)
def calculate_sum(a):
        lst=[]
        for x in range (a):
                b=int(str(a)*(x+1))
                lst.append(b)
        print(sum(lst))
main()


def  main():
        num  =  eval(input())
        calculate_e(num)
def calculate_e(num):
        e,t=1,1
        for i in range(1,num+1):
                t=t/i
                e+=t
        print('%.6f'%(e))
main()

ls  =  eval(input())
n  =  eval(input())
#  重复列表元素n次
ls2=ls*n
ls3  =  [x*x  for  x  in  ls2]
#  下面代码去除重复元素
ls4=[]
for  x  in  ls3:
      if x not in ls4:
              ls4.append(x)
print(ls4)

def maxsum(a):
    a.sort
    n=len(a)//2
    a=sum(a[i] for i in range(0,n*2,2))
    return a
nums  =  eval(input())
v  =  maxsum(nums)#调用自定义函数
print(v)
a=input().split(',')
b=eval(input())
c=[]
for x in range(len(b)):
    lst=[]
    lst.append(a[x])
    lst.append(b[x])
    c.append(lst)
print(c)

a=eval(input())
n,m=map(int,input().split(','))
if n <= len(a):
    for x in range(n,m):
        a.pop(x)
    print(a)
else:
    print('error')

def Fibonacci(num,n):
    a,b=1,1
    if n>2:
        for i in range(n-2):
                c=a+b
                a=b
                b=c
    else:
        c=1
    return c
num  =  [1,  1]
n  =  int(input())
print(Fibonacci(num,  n))'''

'''【问题描述】加密数据。从键盘输入一段数字， 加密规则如下：对于每一个位置上的数字进行如下处理： 每位数字加上 5， 然后除以 10 得到的余数代替该数字， 再将第一位和最后一位交换，第二位与倒数第二位交换， 依此类推， 最后输出加密后的数字密码 。
【输入形式】输入一行数字
【输出形式】输出加密后的结果
【样例输入】123
【样例输出】876'''
a=list(input())
d=[]
for x in a:
    b=str((int(x)+5)%10)
    d.append(b)
d.reverse
f=''.join(d)
print(f)
