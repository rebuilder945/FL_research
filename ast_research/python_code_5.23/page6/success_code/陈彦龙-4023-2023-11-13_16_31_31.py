def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
      day=0
      if x>0:
         x=x/2-2
         day+=1
      print(day)

main()


