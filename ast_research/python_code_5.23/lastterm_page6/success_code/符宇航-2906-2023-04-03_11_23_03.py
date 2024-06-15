def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n = total_count
    a = 0
    for i in range(n):
          total_count = total_count-total_count//2-2
          a += 1
          if total_count<= 0:
                break
    print(a)

main()


