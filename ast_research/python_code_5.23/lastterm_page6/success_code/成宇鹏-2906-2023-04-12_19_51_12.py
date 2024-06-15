def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a = total_count
    x = 0
    while a >= 0:
        a  = a//2 -2
        x += 1 
    print(x)
main()


