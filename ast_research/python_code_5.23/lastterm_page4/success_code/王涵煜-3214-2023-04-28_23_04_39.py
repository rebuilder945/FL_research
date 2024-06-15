num=eval(input())
n=num.count(0)
for i in range(n):
    num.remove(0)
    num.append(0)
print(num)

