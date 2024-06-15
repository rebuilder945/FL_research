def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a)：
      ls1=[] 
      for x in range(0,a):
           a=a*10**x  
           ls1.append(a)
      b=int(sum(ls1))
      print(b)
main()

