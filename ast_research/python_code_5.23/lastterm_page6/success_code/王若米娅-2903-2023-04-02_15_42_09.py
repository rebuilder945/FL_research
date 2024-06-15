def main():
    num = eval(input())
    calculate_e(num)
 
    print("%.6f"%(calculate_e(num)))   
def factorial(x):
    if x==0:
        return 1
    else:
        return x* factorial(x-1)
def calculate_e(x):
    b=0
    for i in range(x):
        c=1/factorial(i)
        b+=c
    return b


  
main()


