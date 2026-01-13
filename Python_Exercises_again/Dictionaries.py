8#1)
# car = {
#     "brand" : "Mercedes",
#     "model" : "Class G",
#     "year" : 2025
#     }
# print(car["model"])
# print(car["year"])

#2)
# def merge_dics(d1,d2):
#     d3 = {}
#     for x in d1:
#         d3[x] = d1[x]
#     for y in d2:
#         d3[y] = d2[y]
#     return d3
# d1 = {"a":3,"b":"cat","c":2}
# d2 = {"a":6,"e":45,"b":"dog"}
# merge_dics(d1,d2)
# print(merge_dics(d1,d2))

#3)
# def word_frequency(sentence):
#     word_separator = []
#     word_counter = {}
#     word_merger = ""
#     for x in sentence:       
#         if x == " ":
#            word_separator.append(word_merger)
#            word_merger = ""
#            continue
#         word_merger += x   
#     word_separator.append(word_merger)

#     for y in range(0, len(word_separator)):
#         dup = False
#         z = 0
#         while z < y:
#             if word_separator[z] == word_separator[y]:
#                 word_counter[word_separator[y]] += 1
#                 dup = True
#                 break
#             z += 1
#         if dup == False:
#             word_counter[word_separator[y]] = 1
        
#     return word_counter
        

# wordis = word_frequency("my name is my name")
# print(wordis)

#4)
# def count_letters(word):
#     letter_count_d = {}
#     for x in range(0, len(word)):
#         if word[x] in letter_count_d:
#             letter_count_d [word[x]] += 1
#         else:
#             letter_count_d [word[x]] = 1
#     return letter_count_d
# wordis = count_letters("banana")
# print(wordis)

#5)
# def most_frequent_letter(word):
#     letter_count_d = {}
#     x = 0
#     most_frequent = word[x]
#     for x in range(0, len(word)):
#         if word[x] in letter_count_d:
#             letter_count_d [word[x]] += 1
#             if letter_count_d [most_frequent] <= letter_count_d [word[x]]:
#                 most_frequent = word[x]
#         else:
#             letter_count_d [word[x]] = 1
#     return most_frequent

# wordis = most_frequent_letter("banana")
# print(wordis)

#6)
# def reverse_dict(d):
#     reverse_d = {}
#     for key in d:
#         reverse_d [d[key]] = key
#     return reverse_d
# dictionary = reverse_dict({"a": 1, "b": 2, "c": 3})
# print(dictionary)

#7)
# def max_value_key(d):
#     first = True
#     for key in d:
#         if first:
#             highest_key = key
#             highest_value = d[highest_key]
#             first = False
#         if d[key] > highest_value:
#             highest_value = d[key]
#             highest_key = key
#     return highest_key

# highest = max_value_key({"a": -21, "b": 0, "c": -2})
# print(highest)

#8)
# def filter_greater_than(d, n):
#     greater_keys = {}
#     for key, value in d.items():
#         if value > n:
#             greater_keys [key] = value
#     return greater_keys

# greater = filter_greater_than({"a": 5, "b": 12, "c": 3}, 5)
# print(greater)

#9)
# def word_frequency(sentence):
#     word_separator = []
#     word_counter = {}
#     word_merger = ""
#     for x in sentence:       
#         if x == " ":
#            word_separator.append(word_merger)
#            word_merger = ""
#            continue
#         word_merger += x   
#     word_separator.append(word_merger)

#     for y in range(0, len(word_separator)):
#         if word_separator[y] in word_counter:
#             word_counter[word_separator[y]] +=1
#         else:
#             word_counter[word_separator[y]] = 1
        
#     return word_counter
        

# wordis = word_frequency("my name is my name")
# print(wordis)

#10)
# def char_frequency(sentence):
#     char_count = {}
#     for y in range (0, len(sentence)):
#         if sentence[y] == " ":
#             continue
#         if sentence[y] in char_count:
#             char_count[sentence[y]] += 1
#         else:
#             char_count[sentence[y]] = 1
#     return char_count

# char_print = char_frequency("hello world")
# print(char_print)

#MINI CHALLENGE)
# def first_unique_char(word):
#     unique_char = ""
#     char_count = {}
#     for y in range (0, len(word)):
#         if word[y] in char_count:
#             char_count[word[y]] += 1
#         else:
#             char_count[word[y]] = 1
#     for z in word:
#         if char_count[z] < 2:
#             unique_char = z
#             break
#     if unique_char == "":
#         unique_char = None
#     return unique_char

# char_print = first_unique_char("wwoorrd")
# print(char_print)