def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ass=[str(a)*x for x in range(1,a+1)]
    pussy=map(int,ass)
    s=sum(pussy)
    print(s)

main()

