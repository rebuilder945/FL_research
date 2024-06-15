def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    b=0
    for i in range(a):
        b+=a*(10**i)
        sum+=b
    print(sum)
main()

