def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    for i in range(a):
    sum+=(a*10**i)*(3-i)
    print(sum)
main()

