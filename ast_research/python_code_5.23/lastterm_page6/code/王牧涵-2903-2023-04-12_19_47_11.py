def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      e=0
      m=0
while m<=num:
     e+=1/m!
     m+=1
print(e)
main()


