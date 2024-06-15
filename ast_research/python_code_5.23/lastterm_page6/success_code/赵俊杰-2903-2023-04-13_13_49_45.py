def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
      while num>0:
            e=1+1/num
            num=num-1
      print("%.6f"%(e))

main()


