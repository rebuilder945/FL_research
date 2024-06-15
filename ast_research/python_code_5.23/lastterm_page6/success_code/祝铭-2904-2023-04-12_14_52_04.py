def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    m = 0
    for i in range(x):
        m = m+10**i*x*(x-i)
    print(m)
main()

