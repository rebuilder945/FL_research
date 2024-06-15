n= eval(input())
n=[int(num) for num in n]
a = round(sum(n)/len(n), 2)
print("{:.2f}".format(a))
