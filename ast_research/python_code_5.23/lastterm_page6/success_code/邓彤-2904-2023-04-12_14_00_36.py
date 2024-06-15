def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(1,a+1):
        t=0
        for j in range(i):
            t=10**j
            s=s+(a*t)
    print(s)
main()

