#每位数字加上 5， 然后除以 10 得到的余数代替该数字， 再将第一位和最\
#后一位交换，第二位与倒数第二位交换， 依此类推， 最后输出加密后的\
#数字密码 。
num=eval(input())
n=num
list=[]
while num>0:
    a=(num%10+5)%10
    list.append(a)
    num=num//10
list.reverse()
a,b,c,d=list[0],list[-1],list[1],list[-2]
list[0]=b
list[-1]=a
list[1]=d
list[-2]=c
word=str(list[0])
for i in range(1,len(list)):
    word=word+str(list[i])
print(word)

