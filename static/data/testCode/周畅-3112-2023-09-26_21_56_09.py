a=int(input())
b=eval(input())
c=eval(input())
numbers=a+b+c
和=sum(numbers)
平均数=sum(numbers)/len(numbers)
结果="%d,%.2f"%(和,平均数)
print(结果)
