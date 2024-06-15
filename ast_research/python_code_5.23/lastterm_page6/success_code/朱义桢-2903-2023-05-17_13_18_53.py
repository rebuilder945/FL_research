def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    a=[1]
    for x in range(n):
        b=1
        for i in range(x):
            b=b/(i+1)
        a.append(b)
    print("%.6f"%(sum(a)))
main()


