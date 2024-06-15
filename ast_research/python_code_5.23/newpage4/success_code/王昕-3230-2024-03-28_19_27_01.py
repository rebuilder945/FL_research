# a=eval(input())
# a.sort(reverse=True)
# a_str="".join(a)
# b=int(a-str)
# print(b)


#方法一
# f=eval(input())
# f.sort(reverse=True)
# num=len(f)
# m=""
# for i in range(num):#一般指代着有限次的循环
#     x=str(f[i])
#     m=m+x
# print(int(m))



#方法二
f=eval(input())
f.sort(reverse=True)#重点备注：sort这样的函数会直接改变变量本身并且不需要赋值
a=list(map(str,f))
print("".join(a))#join函数无法改变函数本身，需要赋值来体现函数的应用

#方法三
# f=eval(input())
# f.sort(reverse=True)
# a = [str(i) for i in range(f)]
# print(a)

