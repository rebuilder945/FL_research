def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e = 1
    for i in range(1,n+1):
        a = 1
        for j in range(1,i+1):
            a*=j
        e = e + 1/a
    print("%.6f"%(e))
main()


