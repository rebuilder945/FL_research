def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    count=0
    while a>0:
        a=a-a//2-2
        count+=1
    print(count)
main()


