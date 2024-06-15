def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    n=1
    s=0
    for i in range(a):
        a=a*n
        n=n*10
        s=s+a
    return s
main()

