# fruits=['grape','pear','apple','water melon']
# fruitsSorted=sorted(fruits,reverse=True)
# print("fruitsSorted:",fruitsSorted)
# print("fruits:",fruits)


# v1=[x for x in range( -5,+10,2 )]
# v2= "".join([chr(ord('a')+x )for x in range(26)])
# print("v1:",v1)
# print("v2:",v2)
# print(v1[:5])
# print(v1[-6:-1])
# print(v1[-1:-7:-2])
# print(v2[:])
# print(v2[::-5])
# print(v2[::-1])
# print(v2[:-5:7])


# print(list(range(4)))
# print(list(range(7,11)))
# print(list(range(1,14,3)))
# print(list(range(15,2,-4)))
# print(list(range(-20,20,6)))
# print(list(range(-1,-22,-7)))

#组合扑克牌
# suits=['红','梅','黑','方']
# ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# cards=[x+y for x in suits for y in ranks]
# print(cards)

#闰年与平年的判定
# years=int(input())
# if years%4==0:
#     if years%400==0:
#         print('闰年')
#     else :
#         if years%100==0:
#             print('平年')
#         else:
#             print('闰年')
# else:print('平年')


#超速罚款
# v=eval(input())
# l=eval(input())
# if v<=l:
#     print('未超速')
# else:
#     if v/l-1<=0.1:
#         print('超速警告')
#     elif 0.1<v/l-1<=0.2:
#         print('罚款100元')
#     elif 0.2<v/l-1<=0.5:
#         print('罚款500元')
#     elif 0.5<v/l-1<=1:
#         print('罚款1000元')
#     elif v/l>1:
#         print('罚款2000元')


# v=[7,11,13]
# print(max(v))
# print(min(v))
# print(sum(v))
# print("%.2f" %(sum(v)/len(v)))


# fruits=['grape','pear','apple','water melon']
# fruits.reverse()     #sort(key=len) 长度排序    reverse(）倒序
# print("reversed fruits:",fruits)


# a=[1,2,3,4,5,6,7]
# b=a
# c=a[:]
# a[3:5]=99,100
# print("a=",a,id(a)==id(b))
# print("b=",b)
# print("c=",c,id(c)==id(a))


# def costCompute(istart,iEnd):
#     iConsume =iEnd -istart
#     return iConsume*0.85
# fElecFee1 =costCompute(1201,1786) 
# fElecFee2 = costCompute( 1322,1423)
# print("Electric Power Cost of Mr Zhang:",fElecFee1)
# print("Electric Power Cost of Mr Lee:",fElecFee2)



# GDP = {"CN":15.63,"US":20.9,"DE":3.78,"JP":5.13}
# GDP["UK"] = 2.59 
# GDP["JP"] = 5.23
# del GDP["DE"]
# GDP1= GDP 
# print(GDP==GDP1)
# print(GDP is GDP1)
# GDP1 = GDP.copy() 
# print(GDP1)
# print(GDP==GDP1)
# print(GDP is GDP1)
# print("CN" in GDP)
# print(20.9 in GDP)
# print(GDP["CN"])
# print(GDP.get("CN",999))
# print(GDP.get("FR",0))
# GDP2={"IT":1.84,"ES":1.24,"DE":2.78,"JP":5.23} 
# GDP.update(GDP2)
# print(GDP)
# {'CN': 15.63, 'US': 20.9, 'JP': 5.23, 'UK': 2.59, 'IT': 1.84, 'ES': 1.24, 'DE': 2.78}
# GDP.clear()
# print(GDP)
# def  insert(num,array1):  #把整数num插入非递减顺序列表array1，插入后仍然保持非递减顺序不变
#         place=0    
#         for  x  in  array1:
#                     if  num<x:    #找到array1里面第一个比num大的数
#                             break
#                     else:
                            
#                         place=array1.index(x)+1
#     #更新place
#         return  array1[:place]  +[num]+array1[place:]    #num插入array1的place位置
        
# def  mysort(array2):    #该函数实现递归的插入排序
#         temp=[]
#         if  len(array2)==1:  #递归结束条件
#                 return  array2
#         else:
                
#                 temp=mysort(array2[:len(array2)-1])
#           #对除去最后一个元素的列表进行插入排序
#                 temp=insert(array2[-1],temp)  #把最后一个数插入到前面排好序的列表里
#                 return  temp
              
# origin=input().split()
# for  x  in  range(len(origin)):
#         origin[x]=eval(origin[x])
# result=mysort(origin)
# for  x  in  result:
#         print(x,end="  ")
# def  merge(array1,array2):# 该函数用来将两个有序序列合并成一个有序序列
#         array3=[]    #合并的列表
#         p1=p2=0    #两个搜索位置，一个搜索  array1,  一个搜索array2
#         while  p1<len(array1)  and  p2<len(array2):    #两个列表都没有搜索完
#                 if  array1[p1]<array2[p2]:      #p1位置的array1元素比p2位置的array2元素小
#                         array3.append(array1[p1])    
#                         p1+=1    #  搜索array1的下一个元素
#                 else:    
                        
#                         array3.append(array2[p2])
#                         p2+=1

#         if  p1==len(array1):    #array1先搜索完
#                 array3=array3+array2[p2:]      #处理array2剩余的部分
#         else:      #array2先搜索完
#                 array3=array3+array1[p1:]
#         return  array3
        
# def  mysort(mylist):  #该函数实现递归的归并排序
#         if  len(mylist)<=1:    #  递归结束条件
#                 return  mylist
#         middle=len(mylist)//2                
        
#         left_list=sorted(mysort(mylist[:middle]))
#         right_list=sorted(mysort(mylist[middle:]))
#               #对列表的左半部分和右半部分分别做归并排序
#         return  merge(left_list,right_list)

# origin=input().split()
# for  x  in  range(len(origin)):
#           origin[x]=int(origin[x])
# result=mysort(origin)
# for  x  in  result:
#           print(x,end="  ")
# def  GCD(m,n):  
#         if  n==0:            #递归结束条件
#                 return m

#         else:
                    
                
#                return GCD(m=n,n=m%n)


# a,b=eval(input())
# d=GCD(a,b)    #调用自定义函数
# print(d)

# def zhao(lst,a):
#         s=0
#         if a==1:
#                 s+=len(lst)
        
#         for i in lst:
#                 if type(i)==list:                                                       
#                      s+=zhao(i,a-1)  
#         return s

# ls=eval(input())
# n=int(input())
# m=zhao(ls,n)

# print(m)


#读取文本中的行与列并且将矩阵生成嵌套列表
# d = []
# with open('cellpicture.txt') as f:
#     m,n = map(int,f.readline().split())
#     for x in range(m):
#         r = list(map(int, f.readline()[:n]))
#         d.append(r)                          
# #自定义函数，查找相邻区域是否为细胞的一部分       
# def explorePixel(d,m,n,i,j):
#         q = [(i,j)]
#         while q:
#             x,y = q.pop(0)
#             if d[x][y] < 0:
#                 continue 
#             d[x][y] = 0-d[x][y]#将已探索区域标记
#             if x>0 and d[x-1][y]>0:        #将探索点周围符合要求的区域加入待探索部分
#                 q.append((x-1,y))
#             if x<(m-1) and d[x+1][y]>0:
#                 q.append((x+1,y))
#             if y>0 and d[x][y-1]>0:
#                 q.append((x,y-1))
#             if y<(n-1) and d[x][y+1]>0:
#                 q.append((x,y+1))
# iCellCount = 0
# for i in range(m):
#     for j in range(n):
#         if d[i][j] <= 0:    #遍历嵌套列表，从查找到的待探索区域进行深层次探索，查找完整细胞
#             continue
#         iCellCount += 1
#         explorePixel(d,m,n,i,j)

# print(iCellCount)






# sname=input()
# f=open(sname,'r')
# k=f.read().upper()
# f.close()
# f=open(sname,'w')
# f.seek(0)
# f.write(k)
# f.close()
# f=open(sname,'r')
# print(f.read())
# def  main():
#         stra  =  input()
#         lista=  list(stra)
#         print(replace_stars(lista))

# def  replace_stars(  str_list):    #  将所有*号移动到数组的左侧
#         j  =  len(str_list)  -  1
#         for  i  in  range(len(str_list)  -  1,  -1,  -1):
#                 if  str_list[i]  !=  '*':
                        
#                 
#                     j  -=  1
#         return  str_list
# main()

# id=input()
# if len(id)<18:
#      print('Error')
# else:
          
#         nn=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
#         kk=0
#         for i in range(17):
#                 kk+=nn[i]*int(id[i])
#         yu=kk%11
#         car=[1,0,10,9,8,7,6,5,4,3,2]
#         dic={}
#         for i in range(11):
#                 dic[i]=car[i]
       
#         if id[17]=='X':
#                 z=10
#         else: z=int(id[17])
#         if dic[yu]==z:
        
#                 print('Correct')
#         else:
#                 print('Wrong')

words=input()
str=''
for i in range(len(words)):
    if words[i].isdigit():
        j=i
        str1=''
        while words[j].isdigit():
            str1+=words[j]
            j+=1
            if j>=len(words):
                break
        if len(str1)>len(str):
            str=str1
print(str)
    
    
