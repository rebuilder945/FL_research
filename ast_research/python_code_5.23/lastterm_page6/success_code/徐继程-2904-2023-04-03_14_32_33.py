def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    for i in range(a):
        sum+=a
        a=str(a)
        a=a+a
        a=int(a)
    print(a)
main()

