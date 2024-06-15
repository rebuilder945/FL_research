def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(a):
        b=sum(sum(a*10**i))
    print(b)
main()

