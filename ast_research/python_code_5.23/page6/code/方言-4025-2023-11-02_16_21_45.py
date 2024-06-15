def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
  n=num;e=0
  for i in range(1,n+1):
  e+=1/i!
  print(e)
main()


