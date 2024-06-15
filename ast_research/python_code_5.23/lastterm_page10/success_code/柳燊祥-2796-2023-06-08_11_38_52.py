s=input()
def num_str(n):
    start,end=0,0
    longest_length, current_length=0,0
    for i in n:
        if i.isdigit():
            current_length+=1
            end=i
            if current_length>longest_length:
                longest_length=current_length
                start=int(end)-int(longest_length)+1
        else:
            current_length=0
    return n[start:start+longest_length]
print(num_str(s))
        

