def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a = []                            
    s = 0                             
    for i in range(1, count+1):       
        a.append(num*i)               
        s += int(num*i)               
    print(f"{s} = {'+'.join(a)}") 

main()

