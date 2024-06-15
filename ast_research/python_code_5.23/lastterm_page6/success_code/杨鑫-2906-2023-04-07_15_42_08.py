def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    b = 0
    while a>0:
        b = b+1
        a = a-a//2-2
    print(b)
    
main()


