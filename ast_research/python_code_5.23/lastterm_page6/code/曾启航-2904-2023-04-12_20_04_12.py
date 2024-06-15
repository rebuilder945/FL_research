def main():
    a=int(input())
    calculate_sum(a)
 def calculate_sum(a):
  jishu=0
  b=0
  while jishu<=a:
   b=b+a*10**jishu
   jishu=jishu+1
  else: print(b)
main()

