def main():
    total_count = int(input())
    calculate_days(total_count)
from math import floor
def calculate_days(a):
    n=0
    while a>0:
        a=a-floor(a/2)-2
        n+=1
    print(n)
main()


