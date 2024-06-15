def main():
    num = eval(input())
    calculate_e(num)
def jiechen(q):
    d=1
    for n in range(1,q+1):
        d *= n   
    return d    
def calculate_e(i):
    sum = 1
    for x in range(1,i+1):
        sum += 1/jiechen(x)
    print("%.6f"%(sum))
main()


