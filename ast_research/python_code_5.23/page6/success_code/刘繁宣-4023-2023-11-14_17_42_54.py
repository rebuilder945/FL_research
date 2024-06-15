def main():
    total_count = int(input())
    calculate_days(total_count)
from math import floor
def calculate_days(t):
    n=0
    while t>0:
          t=t-floor(t/2)-2
          n+=1  
    print(n)
main()


