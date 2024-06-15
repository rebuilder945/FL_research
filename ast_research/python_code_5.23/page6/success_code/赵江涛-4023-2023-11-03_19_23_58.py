def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
     d = 0
     h = total_count
     while h > 0:
          h = h/2-2
          d+=1
     print(d)
main()


