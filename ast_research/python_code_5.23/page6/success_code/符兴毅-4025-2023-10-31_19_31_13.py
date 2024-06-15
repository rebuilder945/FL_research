def main():
    num = eval(input())
    calculate_e(num)
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
def calculate_e(num):
    e = 1
    for i in range(1,num+1):
        e += 1/fact(i)
    print("%.6f"%e)

main()


