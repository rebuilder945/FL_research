def shuixian(x):
    jihe = [int(k) for k in str(x)]
    for j in jihe:
        if int(x) == sum(j**3):
            print(int(x))

n = int(input())
if n<100 or n>999:
    print("none")
elif n>=100 and n<=999:
    for x in range(n):
        shuixian(n)
