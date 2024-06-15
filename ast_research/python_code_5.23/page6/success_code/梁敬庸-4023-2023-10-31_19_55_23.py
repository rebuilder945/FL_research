def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(c):
    n=0
    while c>0:
        n+=1
        c=c*0.5-2
    print(n)
main()


