def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
        for i in range (1,10000):
            if total_count == 1 or total_count == 2:
                  print(i+1)
                  break
            else:
                if total_count %2 != 0:
                        total_count = (total_count+1)*1/2-2
                        if total_count == 0 :
                            print(i)
                            break
                else:
                      total_count = (total_count)*1/2-2
                      if total_count == 0 :
                        print(i)
                        break
main()


