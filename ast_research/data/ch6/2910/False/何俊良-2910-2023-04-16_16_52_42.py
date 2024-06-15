def calculate_distance(h,n):
    distance = h
    bounce_height = h / 2
    for i in range(1, n):
        distance += bounce_height * 2
        bounce_height /= 2
    return distance    
