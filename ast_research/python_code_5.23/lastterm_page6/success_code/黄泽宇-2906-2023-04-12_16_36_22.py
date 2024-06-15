def main():
    total_count = int(input())
    calculate_days(total_count)
def   calculate_days(total_count):
 n=0
 if total_count-(total_count//2)+2 >= 0 :
  n+=1
 else:
  print(n)
main()


