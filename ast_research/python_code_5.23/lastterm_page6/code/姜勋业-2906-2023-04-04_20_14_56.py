def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
       day = 1
       while 1:
       num = a-a/2-2
       if num < 1:
       break
       day += 1
       print(day)
main()


