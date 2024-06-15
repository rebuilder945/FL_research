n=eval(input())
num=[x for x in range(1,n+1)]
num.insert(len(num),1)
num.remove(1)
print(num)
