def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    b = 1
    while a>0:
        a = int(a/2)-2 
        b = b+1
    if a<=0:
        print(b)
main()


