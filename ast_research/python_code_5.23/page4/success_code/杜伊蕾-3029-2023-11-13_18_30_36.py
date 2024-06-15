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
print(v)'''
a=input().split(',')
b=eval(input())
lst=[]
for x in range(len(b)):
    c=[]
    lst.append(a[x])
    lst.append(b[x])
    c.append(lst)
print(c)

