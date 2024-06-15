def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      sum = 1
      for i in range(1,num+1):
            sum += 1/i!
      print(sum)
main()


