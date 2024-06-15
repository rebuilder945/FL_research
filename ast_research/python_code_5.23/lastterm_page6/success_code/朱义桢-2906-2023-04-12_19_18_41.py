def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    a=0
    for i in range(n):
        n=n/2-2
        a+=1
        if n<=0:
            print(a)
            break
main()


