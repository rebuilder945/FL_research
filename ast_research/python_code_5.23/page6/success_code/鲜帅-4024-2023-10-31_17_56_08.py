def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    n=0
    m=0
    for i in range(x):
        n=n*10+x
        m+=n
    print(m)
main()

