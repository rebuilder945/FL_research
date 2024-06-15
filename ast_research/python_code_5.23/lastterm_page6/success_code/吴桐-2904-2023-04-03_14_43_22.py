def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    s=0
    n=0
    for i in range(a):
        n=n+a*10**i
        s=n+s
    print(s)
main()

