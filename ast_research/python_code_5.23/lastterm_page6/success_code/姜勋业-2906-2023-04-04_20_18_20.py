def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
      days = 0
      while True:
                 total_count = total_count - (total_count // 2 + 2)
                 days += 1
                 if total_count <= 0:
                    break
      print(days)
main()


