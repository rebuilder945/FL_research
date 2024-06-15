def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=a
    sum=0
    for i in range(a):
        sum+=x
        x=x*10+a
    print(sum)

main()

