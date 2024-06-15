def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(0,a+1):
        t = 10**i*(a-i)*a
        s=t+s
        if a-i ==0:
            break
    print(s)
main()

