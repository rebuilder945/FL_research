def shui(num):
    if num in range(100,1000):
        i=num//100 # 153/100等于1.53，应该整除，把后面的小数去掉，这就是百位数
        j=num//10%10 # 153//10等于15，再对15/10取余即可得出十位数5
        k=num%10 # 153%10取余
        if (i**3 +j**3 + k**3 == num):
            return True
        else:
            return False
    else:
        return False
n=eval(input())
m=[]
if n not in range(100,1000):
    print('none')
else:
    for i in range(100,n+1):
        if shui(i):
            print(i)
            m.append(i)
    if m==[]:
        print('none')

