# a=input()
# la=len(a)
# lst=[]
# for i in range(la):
#     lst.append(a[i])

# for i in lst:
#     if lst.count(i)==1:
#         print(i)
#         break
# else:
#     print('None')


# def f(l,n,deep):
#     conut=0
#     for i in l:
#         if n==deep:
#             conut+=1
#         if n<deep and type(i)==list:
#             conut+=f(i,n+1,deep)
#     return conut
# l=eval(input())
# deep=int(input())
# print(f(l,1,deep))
# def classify(x,ls):

#     a=[]
#     b=[]
#     for i in ls:
#         if i >x:
#             b.append(i)
#         else:
#             a.append(i)
#     dic['k1'],dic['k2']=a,b
	
# x = int(input())
# ls = input().split()
# ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
# dic = {}

# classify(x,ls)

# print(sorted(list(dic.items())))


a=input()
st=''


for i in a :
    print(i)
    if i>='a'and i<='z' :
        b=ord('z')-ord(i)
        
        st+=chr(ord('a')+b)
        
    elif 'Z'>=i>='A':
        
        
        st+=chr(ord('A')+ord('Z')-ord(i))
    else:
        st+=i
print(a)
print(st)

