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



m=eval(input())
n=eval(input())
if m<0 or n<0:
    print("illegal data")
elif m==n:
    print("It's a square")
else:
    print("It's a rectangle")








