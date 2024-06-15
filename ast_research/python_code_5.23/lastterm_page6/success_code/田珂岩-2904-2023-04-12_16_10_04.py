def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n = 0
    m = 0
    s = 0
    while m < a:
        n += a*10**m
        m += 1
        s += n 
    print(s)
main()

