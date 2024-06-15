'''加密数据。从键盘输入一段数字， 加密规则如下：对于每一个位置上的数字进行如下处理：
 每位数字加上 5， 然后除以 10 得到的余数代替该数字， 再将第一位和最后一位交换，第二位与倒数第二位交换，
  依此类推， 最后输出加密后的数字密码 。
【输入形式】输入一行数字
【输出形式】输出加密后的结果'''
num = list(input())
num1=[]
sum=""
for i in range(len(num)):
    num[i] = (int(num[i])+5)%10
for x in range(len(num)):
    num1.append(num[len(num)-x-1])
    sum+=str(num1[x])
print(sum)

