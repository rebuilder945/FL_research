def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
     soldcount = 0
     remainingcount = total_count
     days = 0
     while remainingcount > 0:
          soldcount = remainingcount // 2 + 2
          remainingcount  -= soldcount
          days += 1
     print(days)
main()


