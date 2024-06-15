def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
      e=1
      while num>0:
            e=1+1/num
            num=num-1
      print(e)

main()


