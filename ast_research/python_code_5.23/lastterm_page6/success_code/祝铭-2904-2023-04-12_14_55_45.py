def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    m = 0
    if 0 < x < 10:
        for i in range(x):
            m = m+10**i*x*(x-i)
        print(m)
    else:
        for j in range(x):
            m = m+100**j*x*(x-j)
        print(m)
main()

