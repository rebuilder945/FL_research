def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    day = 1
    while x > 0:
         a = x/2+2
         x = x - a
        day += 1
        
main()


