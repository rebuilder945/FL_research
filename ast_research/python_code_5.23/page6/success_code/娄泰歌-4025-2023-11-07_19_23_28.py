def main():
    num = eval(input())
    calculate_e(num)
def z(x):
   jishu=1
   eva=1
   while jishu<=x:
      eva*=jishu
      jishu+=1
   return eva
def calculate_e(x):
   eva=1
   jishu=1
   while x>0:
      eva+=1/z(jishu)
      jishu+=1
      x-=1
   print("%.6f"%eva)
main()


