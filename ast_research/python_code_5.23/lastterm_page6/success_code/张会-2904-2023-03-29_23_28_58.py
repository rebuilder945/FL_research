def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    if a <10:
        for i in range(0,a):
            t = 10**i * (a-i) * a
            s=t+s
    else:
        for i in range(0,a):
            t = 10**(i+i) * (a-i) *a
            s=t+s
    print(s)
main()

