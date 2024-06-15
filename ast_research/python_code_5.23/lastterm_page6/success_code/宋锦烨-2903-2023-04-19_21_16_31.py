def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
  e=0
  nn=1
  for i in range(a):
    for j in range(1,i+1):
      nn=nn*j
    e=e+1/nn
    nn=1
  print('%.6f' %e)
  
main()


