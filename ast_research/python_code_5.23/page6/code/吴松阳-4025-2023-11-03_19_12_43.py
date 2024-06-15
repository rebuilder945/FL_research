def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num)：
  e = 1
  a = 1
  for i in range(1,num+1):
    for x in range(1,i+1):
      a = a*(1/x)
    e = e + a
print('{:.6f}'.format(e))
      
    
main()


