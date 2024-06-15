# print('How beautiful you are')
# n=3
# fPrice=3.6
# fMount=n*fPrice
# fMoney=20
# fMoney=fMoney-fMount
# sText1="我买了"
# print(sText1,n,"斤苹果，每斤",fPrice,"元,一共花了",fMount,"元,妈妈给我20元,还剩下",fMoney,"元。")
# # print("%s%d斤苹果，每斤%.2f元."%(sText1,n,fPrice))
# def Circleinfo(round):
#     Pi=3.14
#     r=float(round)
#     return 2*Pi*r,Pi*r*r
# round=float(input("请输入半径:"))
# L,S=Circleinfo(round)
# print("圆的周长是：%.3f"%(L))
# print("圆的面积是：%.4f"%(S))
# print("My favorite sports are as follows:\n\tfootball\n\ttabletennis\n\tbadminton\n\tswimming\n\trunning")
# print("人口类")

# fruits=['grape','pear','apple','water']
# fruitsorted=sorted(fruits,reverse=True)
# print("fruitsorted:",fruitsorted)
# print("fruits:",fruits)
# dummy=['1','s','1']
# print("%d"%(dummy.count('1')))




# a = input()
# b = "".join(set(a))
# print(b[::-1])
# a=eval(input())
# b=a.reverse()
# c=[]
# for i in a:
#     if i not in c:
#         c.insert(0,i)
# print(c)
# a=input()
# if a[0]=='-':
#     b=a[:0:-1]
#     b=0-eval(b)
# else :
#     b=a[::-1]
# print(int(b))
# n,m,l=map(eval,input().split(","))
# b=[]
# for i in range(m):
#     c=n+i*l
#     b.append(c)
# print(b)


#loan.py
# fBalance = 10000 #贷款初始余额
# fRate = 0.0005 #日利万分之五
# balances = [] #贷款余额列表
# for i in range(365*30):
#     fBalance = fBalance + fBalance*fRate #贷款余额 = 本金 + 本金*利率
#     balances.append(fBalance) #把贷款余额存入列表绘图用
# print("30年后连本带利欠款总额: %.2f" % fBalance)


# import random #随机数模块
# N,nHits = 10000000,0 #总投点数，圆内投点数
# xs,ys = [],[] #投点的x,y坐标列表
# for i in range(N): #N次投点
#     x = random.random()*2-1 #随机数取投点坐标[0,1)
#     y = random.random()*2-1
#     xs.append(x) #投点坐标存入列表
#     ys.append(y)
#     if x*x+y*y <= 1: #投点位于内切圆内
#         nHits += 1 #圆内投点数 + 1
#         pi = 4*nHits/N #通过计算圆面积估算圆周率
# print("pi =",pi)


#everest.py
# iCounter = 0 #对折次数
# fThickness = 0.0001 #纸厚，单位米
# while True:
#     if fThickness > 8844.43: #超过珠峰高度就停止循环
#         break
#     else:
#         fThickness *= 2 #对折一次厚度翻倍
#         iCounter += 1 #对折次数加1
# print("纸对折%d次后的厚度为%.2f米,超过了珠穆朗玛峰." % (iCounter,fThickness))

# counts={}
# a=''
# while a!="#":
#     a=input()
#     for i in a:
#         counts[i]=counts.get(i,0)+1
# list=list(counts.items())
# list.sort(key=lambda x :x[1],reverse=True)
# print(list)
        
lst=list(eval(input()))
n, m=eval(input())
if n<=len(lst)-1:
    x=lst[n]
    for i in range(m):
        lst. append(x)
    print(lst)
else:
    print('error')
