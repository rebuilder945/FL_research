def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      lst=[]
      for i in range(a):
           b=int(str(a)*(i+1))
           lst.append(b)
      s=sum(lst)
      print(s)
main()

