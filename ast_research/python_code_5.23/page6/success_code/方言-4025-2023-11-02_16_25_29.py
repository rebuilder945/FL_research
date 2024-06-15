def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
  n=num;l=0;s=1
  for i in range(1,n+2):
    l+=s
    s=s/(i+1)
  print("%.6f"%(l))
main()


