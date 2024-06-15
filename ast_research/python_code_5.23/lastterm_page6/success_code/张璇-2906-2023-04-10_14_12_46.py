def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    i=0
    while a>0:
        b=int(a/2)
        a=a-b-2
        i=i+1
    print(i)
main()


