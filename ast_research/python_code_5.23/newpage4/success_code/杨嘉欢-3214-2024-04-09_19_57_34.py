input=input()
input=input[1:-1]
input=list(map(int, input.split(",")))
zeros=[num for num in input if num==0]
none_zeros= [num for num in input if num !=0]
print(none_zeros+zeros)

        

