def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
        t=1
        m=1
        for i in range(1,n+1):
                m=m*i
                t=t+m
        print("{:.6f}".format(t))
main()


