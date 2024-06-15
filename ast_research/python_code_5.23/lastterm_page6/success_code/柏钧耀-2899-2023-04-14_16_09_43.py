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



a=[]
a=input().split()   
n=int(a[0])
m=int(a[1])

lst=[]
if m-n<2 or n<0 :
    print("illegal input")
elif m>10:
    print("illegal input")
else:
    for i in range(n,m):
        num1=i
        for v in range(n,m):
            if v!=i:
                num2=i*100+v*10
                for z in range(n,m):
                    if z!=v and z!=i:
                        num3=z+num2
                        lst.append(num3)
    print(' '.join(str(i) for i in lst ))

            



        








