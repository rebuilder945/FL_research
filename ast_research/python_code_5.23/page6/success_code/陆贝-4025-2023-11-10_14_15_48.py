def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    z=0
    m=1
    for i in range(1,n+1):
        t=1/m
        z=z+t
        m=m*i
    print("{:.6f}".format(z))
main()


