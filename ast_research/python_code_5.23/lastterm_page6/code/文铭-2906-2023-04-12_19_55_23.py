def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
     x = 0
     while n > 0:
           n= int(n/2)-2
           x+=1
    print(x)
main()


