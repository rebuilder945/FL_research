def main():
    num = eval(input())
    calculate_e(num)
def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)

def calculate_e(num):
     e = 1
     for i in range(1,num+1):
          e += 1/factorial(i)
     print("%.6f"% e)
main()


