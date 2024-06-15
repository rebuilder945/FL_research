n=eval(input())
num=[x for x in range(1,n)]
num.insert(len(num),1)
num.remove(1)
print(num)
