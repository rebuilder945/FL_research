def main():
    num = eval(input())
    calculate_e(num)
      print("%.6f"%(calculate_e(num)))
def calculate_e(num):
    b=[]
    b.append(1)
    for i in range(1,num+1):
        if i == 1:
            y=1/i
            b.append(y)
        else:
            y=1
            for x in range(i):
                y=y*(x+1)
            b.append(1/y)
               
    return sum(b)
main()


