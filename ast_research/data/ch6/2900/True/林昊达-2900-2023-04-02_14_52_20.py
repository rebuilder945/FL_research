# 【问题描述】编写程序，从键盘输入一个数n，输出n以内的所有的回文素数。若n输入不合法（为小数或者负数），则输出提示：“illegal input”。

# 回文素数是指一个数既是素数又是回文数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数称之为素数。例如131既是素数又是回文数。

# 【输入形式】输入一个整数n（n>1）。

# 【输出形式】以空格分隔输出n以内的所有的回文素数。若n输入不合法（为小数或负数），则输出提示“illegal input”

# 【样例输入1】200

# 【样例输出1】2 3 5 7 11 101 131 151 181 191

# 【样例输入2】-4

# 【样例输出2】illegal input


def is_palindrome(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False
def is_prime(n):
    # 遍历从2到n的平方根之间的所有整数，如果有能整除n的，返回False
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    # 否则返回True
    return True
nums = eval(input())
ans=[]
if type(nums) !=type(1) or nums<2:
  print("illegal input")
else:
   for i in range (2,nums+1):
     if is_prime(i) and is_palindrome(i):
       ans.append(i)
   print(" ".join(map(str,ans)))
