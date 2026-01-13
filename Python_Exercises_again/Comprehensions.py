# def get_squares(numbers):
#     squares = [x*x for x in numbers]
#     return squares
# squares_print = get_squares([1, 2, 3])
# print(squares_print)

########################
# def group_even_odd(numbers):
#     even_list = [x for x in numbers if x % 2 == 0]
#     odd_list = [x for x in numbers if x % 2 != 0]
#     return {
#         "even": even_list,
#         "odd": odd_list
#     }
# even_odd_print = group_even_odd([1, 2, 3, 4, 5, 6])
# print(even_odd_print)

########################
# def map_word_lengths(words):
#     return {x: len(x) for x in words}
    
# map_word_print = map_word_lengths(["apple", "pear", "banana"])
# print(map_word_print)


########################
# def score_long_words(words):
#     return {x: len(x) * 10 for x in words if len(x) > 3}
# score_long_print = score_long_words(["hi", "apple", "dog", "python"])
# print(score_long_print)


########################
# def classify_grades(scores):
#     return ["Pass" if x >= 70 else "Fail" for x in scores]
# classify_grades_print = classify_grades([85, 40, 72, 60])
# print(classify_grades_print)


########################
# def unique_lengths(sentence):
#     return {len(x) for x in sentence.split()}
# unique_lengths_print = unique_lengths("the quick brown fox jumps over the lazy dog")
# print(unique_lengths_print)


########################
# def sanitize_data(data):
#     return [0 if item == "N/A" else item * item for item in data]
# exercise = sanitize_data([2, "N/A", 4, 10, "N/A"])
# print(exercise)



########################
# def filter_matrix(matrix):
#     return [num**2 if num > 10 else num for row in matrix for num in row if num % 2 == 0]
# exercise = filter_matrix([
#     [2, 5, 12],
#     [10, 11, 14],
#     [3, 8, 20]
# ])
# print(exercise)



########################
# def vowel_map(words):
#     vowels_dict = {}
#     vowels = set('aeiou')
#     for word in words:
#         found_vowels = set(word.lower()).intersection(vowels)
#         if len(found_vowels) > 2:
#             vowels_dict[word] = found_vowels
#     return vowels_dict
#     # return {word: {vowel for vowel in word.lower() if vowel in 'aeiou'}
#     #          for word in words 
#     #          if len({vowel for vowel in word.lower() if vowel in 'aeiou'}) > 2 }
# exercise = vowel_map(["beautiful", "apple", "queue", "python", "education", "mountain"])
# print(exercise)

def test(items):
    
        return items[len(items)-1]["weight"]
        
    
    
test_test = test([{"item": "sword","weight": 150},{"item": "dagger","weight": 1100},{"item": "staff","weight": 2100}])
print(test_test)