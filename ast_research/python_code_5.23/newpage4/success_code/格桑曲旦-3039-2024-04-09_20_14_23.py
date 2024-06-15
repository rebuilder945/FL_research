def remove_extrems(lst):
    if len(lst)<=2:
        return[]
    else:
        min_val=min(lst)
        max_val=max(lst)
        return[x for x in lst if x !=min_val and x !=max_val]
input_list=[1,2,3,4,5,6,1,7,7]
output_list=remove_extremes(input_list)
print(output_list)
