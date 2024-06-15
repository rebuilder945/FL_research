lst=eval(input())
lst.sort(reverse=True) #sort函数默认升序，reverse接受bool类型的值（True or False）表示是否需要颠倒顺序
i = len(lst)-1 #i表示10的次方,len表示需要计算的字节
sum = 0 #用于求和多个元素
for x in lst:#从大到小开始
    sum = sum+x*(10**i) #**幂的运算
    i=i-1#作为下一次循环，直到停止即有三次循环sum从0-300-320-321
print(sum)
