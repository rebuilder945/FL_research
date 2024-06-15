def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    b = 0
    while a>0:
        b+=1
        a=a-2-a//2
    print(b)
main()


