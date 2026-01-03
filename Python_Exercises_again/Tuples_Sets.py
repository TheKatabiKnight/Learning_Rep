#1)
# def min_max(numbers):
    
#     max_num = 0
#     min_num = 0
#     first = True
#     for x in numbers:
#         if first:
#             min_num = x
#             max_num = x
#             first = False
#         if max_num < x:
#             max_num = x
#         if min_num > x:
#             min_num = x
        
#     min_max_tuple = (min_num, max_num)
#     return min_max_tuple
# exercise_1 = min_max([3, 1, 9, 4])
# print(exercise_1)

#2)
# def remove_duplicates(numbers):
#     no_dupe = []
#     seen = set()
#     for x in numbers:
#         if x not in seen:
#             no_dupe.append(x)
#             seen.add(x)
#     return no_dupe

# exercise_2 = remove_duplicates([1, 2, 2, 3, 1, 4])
# print(exercise_2)

#3)
# def remove_duplicates_and_count(numbers):
#     no_dupe = []
#     seen = set()
#     count_dic = {}
#     for x in numbers:
#         if x not in seen:
#             no_dupe.append(x)
#             seen.add(x)
#             count_dic[x] = 1
#         else:
#             count_dic[x] += 1


#     return no_dupe, count_dic
# exercise_3 = remove_duplicates_and_count([1, 2, 2, 3, 1, 4, 2, 3])
# print(exercise_3)

#4)
# def repeated_numbers(numbers):
   
#     count_dic = {}
#     count_dic2 = {}
#     for x in numbers:
#         if x in count_dic:
#             count_dic[x] += 1
#             count_dic2[x] = count_dic[x]
#         else:
#             count_dic[x] = 1
    
            
#     return count_dic2

# exercise_4 = repeated_numbers([4, 1, 2, 4, 3, 2, 1, 2])
# print(exercise_4)

#5)
def group_even_odd(numbers):
    even_list = []
    odd_list = []
    even_odd_dict = {}
    for x in numbers:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    even_odd_dict["even"] = even_list
    even_odd_dict["odd"] = odd_list
    for key in even_odd_dict:
        return even_odd_dict
exercise_5 = group_even_odd([1, 2, 3, 4, 5, 6])
print(exercise_5)