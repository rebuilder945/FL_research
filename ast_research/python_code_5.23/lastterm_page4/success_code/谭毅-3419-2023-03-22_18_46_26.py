a=[1,2,3,4,5,6,7]
b=a
c=a[0:]
print("a=",a,id(a)==id(b))
print("b=",b)
print("c=",c,id(c)==(a))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

