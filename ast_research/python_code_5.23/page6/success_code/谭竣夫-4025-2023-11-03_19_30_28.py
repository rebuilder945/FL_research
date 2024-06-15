def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      lst=[]
      for i in range(num):
             b=int(str(num)*(i+1))
             lst.append(b)
      print(sum(lst))

main()


