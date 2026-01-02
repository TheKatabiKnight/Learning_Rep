#1)
def min_max(numbers):
    
    max_num = 0
    min_num = 0
    first = True
    for x in numbers:
        if first:
            min_num = x
            max_num = x
            first = False
        if max_num < x:
            max_num = x
        if min_num > x:
            min_num = x
        
    min_max_tuple = (min_num, max_num)
    return min_max_tuple
exercise_1 = min_max([3, 1, 9, 4])
print(exercise_1)
