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
# def group_even_odd(numbers):
#     even_list = []
#     odd_list = []
#     even_odd_dict = {}
#     for x in numbers:
#         if x % 2 == 0:
#             even_list.append(x)
#         else:
#             odd_list.append(x)
#     even_odd_dict["even"] = even_list
#     even_odd_dict["odd"] = odd_list
#     return even_odd_dict
# exercise_5 = group_even_odd([1, 2, 3, 4, 5, 6])
# print(exercise_5)

#6)
# def get_unique_attendees(log_entries):
#     unique_username = {username for time, username, device in log_entries}
#     return unique_username
# unique_attendees = log_entries = get_unique_attendees([
#     ("09:00", "alice88", "laptop"),
#     ("09:05", "bob_22", "phone"),
#     ("09:15", "alice88", "tablet")
# ])
# print(unique_attendees)

#7)
# def clean_and_summarize(data):
#     data_sort = sorted(data)
#     return (data_sort[0], data_sort[-1], data_sort[1:-1])
# cleaned_data = clean_and_summarize([5, 3, 8, 1, 2])
# print(cleaned_data)

#8)
# def summarize_grades(student_data):
#     return [(name, sum(list_of_grades)/len(list_of_grades)) for name, list_of_grades in student_data]
# average = summarize_grades([("Alice", [10, 20]), ("Bob", [30, 40])])
# print(average)

#9)
# def find_positions(target, items):
#     return [position for position, item in enumerate(items) if item == target]
# positions = find_positions("apple", ["apple", "orange", "apple", "banana"])
# print(positions)

#10)
# def create_catalog(names, prices):
#     return [(name, price * 1.1) for name, price in zip(names, prices)]
# catalog_with_tax = create_catalog(["Shirt", "Hat"], [20, 10])
# print(catalog_with_tax)

#11)
# def find_common_friends(user_a_friends, user_b_friends):
#     return (sorted(set(user_a_friends) & set(user_b_friends)), sorted(set(user_a_friends) - set(user_b_friends)))
# common_friends = find_common_friends(["Alice", "Bob", "Charlie"], ["Bob", "David", "Alice"])
# print(common_friends)

#12)
# def parse_record(record):
#     first, *middle, last = record
#     return {"date": first, "readings": sum(middle), "status": last}
# record = parse_record(["2023-10-02", 5, 5, "ERROR"])
# print(record)

#13)
# def get_premium_items(inventory):
#     return {item: price*0.9 for item, price in inventory.items() if price > 100}
# exercise = get_premium_items({"Laptop": 1200, "Mouse": 25, "Monitor": 200, "Cable": 10})
# print(exercise)