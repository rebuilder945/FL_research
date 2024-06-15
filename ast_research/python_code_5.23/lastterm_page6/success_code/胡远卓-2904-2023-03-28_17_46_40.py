def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum,tmp=0,1
    for i in range(a):
        sum+=tmp*(a-i)*a
        tmp*=10
    print(sum)

main()

