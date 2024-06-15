def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e=1
    m=1
    for x in range(n):
       m=m/(x+1) 
       e+=m
    print("%.6f"%(e))
main()


