def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    for x in range(1,a+1):
        for i in range(x):
            s += 10**i
    s = a*s
    print(s)
main()

