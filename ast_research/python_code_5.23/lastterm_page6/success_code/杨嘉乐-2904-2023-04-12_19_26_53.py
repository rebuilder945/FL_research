def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    b=0
    x=a//10
    for i in range(a):
        b+=a*(10**(i*(x+1)))
        sum+=b
    print(sum)

main()

