def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      sum = 1
      n=1
      for i in range(1,num+1):
            n *=i
            sum += 1/n
      print("%.6f"%(sum))
main()


