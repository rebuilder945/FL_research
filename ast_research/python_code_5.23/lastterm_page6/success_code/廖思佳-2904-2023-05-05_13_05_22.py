def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    m=str(a)
    all=0
    for i in range(1,a+1):
        n=int(m*i)
        all+=n
    print(all)

main()

