n = eval(input())
lst = [2,3]
sum = 0
m = 0
if n>=3:
    sum = 2/1+3/2
    for i in range(n-2):
        m = lst[i]+lst[i+1]
        lst.append(m)
        a = m/(i+3)
        sum = sum + a
    print("%.4f"%sum)
elif n == 1:
    sum = 2/1
    print("%.4f"%sum)
elif n == 2:
    sum = 2/1+3/2
    print("%.4f"%sum)
