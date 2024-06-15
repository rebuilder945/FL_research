def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
 e=0
  for i in range (1,num+1):
   e=e+1/i!
  print(e)
main()


