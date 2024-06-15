def main():
    a=int(input())
    calculate_sum(a)

num = input()         
count = int(input())  
a = []                            
s = 0                             
for i in range(1, count+1):       
    a.append(num*i)               
    s += int(num*i)               
print(s) 

main()

