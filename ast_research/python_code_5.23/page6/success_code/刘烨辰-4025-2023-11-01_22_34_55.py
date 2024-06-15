def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    b=1
    e=1
    for i in range(1,n+1):
        b=b*i
        e=1/b+e
    print("%.6f"%e)
main()


