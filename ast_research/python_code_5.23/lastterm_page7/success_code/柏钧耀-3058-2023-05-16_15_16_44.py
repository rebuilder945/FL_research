# a=eval(input())
# a=str(a)
# a=list(a)
# b=[]
# for i in a:
#     i=(int(i)+5)%10
#     b.append(i)
# if len(b)==2:
#     b[0],b[-1]=b[-1],b[0]
# else:
#     b[0],b[-1]=b[-1],b[0]
#     b[1],b[-2]=b[-2],b[1]
# print(''.join(str(i) for i in b))






# a=eval(input())
# b=eval(input())
# c=[]
# if b==1:
#     print('%.2f'%(a))
# else:
#     for i in range(1,b):
#         d=2*a*0.5**i
#         c.append(d)
#     print('%.2f'%(a+sum(c)))




# stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

# ['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

# ['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

# ['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

# ['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
# a=input()
# c=[]
# for i in range(len(stu_list)):
#     for j in range (0,1):
#         if a==stu_list[i][j]:
#             c.append(stu_list[i])
#             print(stu_list[i][0]+stu_list[i][1])
#         else:continue
# if c==[]:
#     print("None")





# a=eval(input())
# n1=1
# b=[1,1]
# n2=0
# if a == 1:
#     pass
# else:
#     n2=1
#     for i in range (a):
        
#         n2+=b[i]
        
#         b.append(n2)
# s=0
# if a==1:
#     print("2.0000")
# else:
#     for i in range (a):
#         s+=b[2+i]/b[1+i]
#     print("%.4f"%(s))







# m=[]
# while True:
#     a=input()
#     if a=="#":
#         print(len(m),sum(m))
#         break
#     else:
#         m.append(eval(a))



        
    

# num=eval(input())
# if int(num)<num:
#     print("illegal input")
# elif num>0:
#     b=[]
#     for i in range(num):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#                 b.append(i)
#                 continue
#     d=[]
#     for i in range(len(b)):
#         h=str(b[i])
   
#         if h == h[::-1]:
#          d.append(b[i])

#     d.remove(0)
#     d.remove(1)
#     print(" ".join(str(x) for x  in d))
# elif num<0:
#     print("illegal input")
# else:
#      print("illegal input")






# m=[]
# m=input().split()
# print(m)



# a=[]
# a=input().split()   
# n=int(a[0])
# m=int(a[1])

# lst=[]
# if m-n<2 or n<0 :
#     print("illegal input")
# elif m>10:
#     print("illegal input")
# else:
#     for i in range(n,m):
#         num1=i
#         for v in range(n,m):
#             if v!=i:
#                 num2=i*100+v*10
#                 for z in range(n,m):
#                     if z!=v and z!=i:
#                         num3=z+num2
#                         if num3>100:
#                             lst.append(num3)
#     print(' '.join(str(i) for i in lst ))



# m=eval(input())

# if m in list(range(1,11))+list(range(19,29)):
#     if  m%2==0:
#         print("black")
#     else :print("red")
# elif m in list(range (11,19))+list(range(29,37)):
#     if m%2==0:
#         print("red")
#     else :print("black")
# elif m==0:
#     print("green")
# else:
#     print("error")




# spr=[3,4,5]
# sum=[6,7,8]
# aut=[9,10,11]
# win=[12,1,2]
# m=eval(input())

# if m in spr:
#     print("spring")
# elif m in sum:
#     print("summer")
# elif m in aut:
#     print("autumn")
# elif m in win:
#     print("winter")
# else:
#     print("error")
            

# a=0
# b=0
# c=0
# d=0

        
# m=input()
# for i in m:
#     if i.isdigit():
#         a+=1
#     elif i.isspace():
#         b+=1
#     elif i.isalpha():
#         c+=1
#     else:
#         d+=1
# print(c,b,a,d)
        

# def f(x):
#     y=0
#     if x<20:
#         y=6*x**2+1
#     elif 40>x>=20:
#         y=(3*x-60)**0.5
#     else:
#         y=100/(x+1)
#     return y
# x=eval(input())

# print("%.2f"%(f(x)))



# m=eval(input())
# n=eval(input())

# if m<=0 or n<=0:
#     print("illegal data")
# elif m==n:
#     print("It's a square")
# else:
#     print("It's a rectangle")


# chinese=eval(input())
# math=eval(input())
# if chinese>=99 and math>=99:
#     print("You won a scholarship of 500 yuan!")
# elif chinese<30 and math<30:
#     print("You need to relearn!")




# n=eval(input())
# m=''.join(n)
# print(m)
# a=set(m)
# print(a)
# b=list(a)
# print(b)
# b.sort()
# for i in b:
#     print("%s,%d"%(i,m.count(i)))


# m=eval(input())
# if m<=100:
#     print("none")
# elif m>1000:
#     for i in range(100,1000):
#         a=int(i/100)
#         b=int(i%100/10)
#         c=int(i%10)
#         if a**3+b**3+c**3==i:
#             print(i)

# else:
#     for i in range(100,m+1):
#         a=int(i/100)
#         b=int(i%100/10)
#         c=int(i%10)
#         if a**3+b**3+c**3==i:
#             print(i)

# 文明经典
# 论文写作（实地考察）
# 数学复习
# 英语论文
# 形式与政策
# 复习python





# grades=eval(input())
# if grades>=90:
#     print("A")
# elif 90>grades>=80:
#     print("B")
# elif 80>grades>=70:
#     print("C")
# elif 70>grades>=60:
#     print("D")
# else:print("E")






# print(list(range(4  )))
# print(list(range(    7,11 )))
# print(list(range(  1,14,3      )))
# print(list(range( 15,2,-4       )))
# print(list(range(    -20,20,6    )))
# print(list(range( -1,-22,-7       )))



# suits=['红','梅','黑','方']
# ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# cards=[x+y for x in suits for y in ranks]
# print(cards)

# year=eval(input())
# if year%4==0:
#     if year%400==0:
#         print("闰年")
#     else:
#         if year%100==0:
#             print("平年")
#         else:
#             print("闰年")
# else:
#     print("平年")





# a={}
# b=[]
# while 1:
#     if "None" in b:
#         break
#     c=input()
#     b.append(c)
# for i in b:
#     a[i]=a.get(i,0)+1
# lst=list(a.items())
# lst.sort(key=lambda x:x[1],reverse=True)
# print(lst)




# a={}

# a[input()]=eval(input())




# s1=eval(input())
# s2=eval(input())
# rate=(s1-s2)/s2
# if rate<=0:
#     print("未超速") 
# elif rate<=0.1:
#     print("超速警告")
# elif 0.1<rate<=0.2:
#     print("罚款100元")
# elif 0.2<rate<=0.5:
#     print("罚款500元")
# elif 0.5<rate<=1:
#     print("罚款1000元")
# elif rate>1:
#     print("罚款2000元")





# v=[7,11,13]
# a=sum(v)/len(v)
# print(max(v))
# print(min(v))
# print(sum(v))
# print("%.2f"%a)


# a=['grape','pear','apple','water melon']
# b=sorted(a,reverse)
# print("fruitsSorted:",b)
# print("fruits:",a)

# a=[1,2,3,4,5,6,7]
# b=a
# c=a[::1]
# a[3:5]=99,100
# print("a=",a,id(a)==id(b))
# print("b=",b)
# print("c=",c,id(c)==id(a))


# print("")
# print("")
# print("v1: [-5, -3, -1, 1, 3, 5, 7, 9]")
# print("v2: abcdefghijklmnopqrstuvwxyz")
# print("[-5, -3, -1, 1, 3]")
# print("[-1, 1, 3, 5, 7]")
# print("[9, 5, 1]")
# print("abcdefghijklmnopqrstuvwxyz")
# print("zupkfa")
# print("zyxwvutsrqponmlkjihgfedcba")
# print("aho0")



# lst=eval(input())
# lst1=lst.copy()
# lst1.sort()

# max=lst1[0]
# min=lst1[-1]
# lst2=[]
# for i in range(len(lst)):
#     if lst[i]!=max and lst[i]!=min:
#         lst2.append(lst[i])
# print(lst2)



# lst=eval(input())
# b=[]
# for i in lst:
#     a=lst.count(i)
#     if a==1:
#         b.append(i)
# b.sort()
# print(','.join(str(i) for i in b))    



# def fac(n):
#     a=1
#     for i in range(n,0,-1):
#         a*=i
        
#     return a
# n=eval(input())

# print(fac(n))




# reverse 递归 


# def  work(a)  :
#     dic={}
#     dic[0]=1
#     for i in range(1,int(a)+1):
#         c=1
#         for j in range(1,i+1):
#             c*=j
#             dic[i]=c
#     return dic
        

# a  =  int(input())
# ans  =  work(a)
# print(ans)



# ls=eval(input())
# cou={}
# for i in ls:
#     cou[i]=cou.get(i,0)+1
# print(cou)



dic={}
lst=[]
while True:
    a=input()
    lst.append(a)
    if a =="q":
        break
    
for i in lst:
    dic[i]=dic.get(i,0)+1
print(dic)
b=list(dic.items())

b.sort(key=lambda x:x[1],reverse=True)
m,n=b[0]
print(m,n)

