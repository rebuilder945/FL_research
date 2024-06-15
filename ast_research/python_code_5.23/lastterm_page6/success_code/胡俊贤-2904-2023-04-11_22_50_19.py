def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    s=0
    for i in range(a):
        a=a*10**i
        s=s+a
    return s
main()

