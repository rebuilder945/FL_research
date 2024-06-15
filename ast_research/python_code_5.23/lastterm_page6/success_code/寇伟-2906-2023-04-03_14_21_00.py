def main():
    total_count = int(input())
    calculate_days(total_count)
from math import *
def calculate_days(w):
    day=0
    while w!=0:
        w=round(w/2)-2
        day+=1
    print(day)
        
main()


