# 1)
# def hello():
#     print('Hello')
# hello()
# hello()
# hello()

#2)
# def greet(name):
#     print('Hello', name)
# greet('Ishak')

#3)
# def add_numbers(x, y):
#     return x + y
# sum = add_numbers(3, 5)
# print('The sum is:', sum)

#4)
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# num_check = is_even(3)
# print(num_check)

#5)
# def max_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# max = max_of_two(13, 21)
# print(max)

#6)
# def word_repeat(word, number):
#     x = 1
#     result = ""
#     for x in range(0, number):
#         result += word
#     return result
# word_rep = word_repeat("Hi", 3)
# print(word_rep)

#7)
# def count_vowels(word):
#     count = 0
#     for x in range (0, len(word)):
#         c = word[x]
#         if c in 'eioua':
#             count += 1
#     return count
# print(count_vowels('engage'))

#8)
# def factorial(num):
#     sum = 1
#     for x in range (1, num+1):
#         sum = sum * x
#     return sum
# facto = factorial(9)
# print(facto)

#9)
# def exponents(num, exponent=2):
#         sum = 1
#         for x in range(0, exponent):
#             sum = sum * num
#         return sum
# print(exponents(5))

#10)
# def fibonacci(num):
#     if num == 0:
#         return []
#     elif num == 1:
#         return [0]
#     fib = [0, 1]
#     for x in range(0, num-2):
#         next_num = fib[-1] + fib[-2]
#         fib.append(next_num)
#     return fib
# print(fibonacci(0))

#11)
# def prime(num): 
#     primes_up = []
#     for x in range (2, num):
#         is_prime = True
#         for y in range (2, x):
#             if x % y == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes_up.append(x)
#     return primes_up
# primes_up_to = prime(20)
# print(primes_up_to)

#12)
# def sum_list(numbers):
#     sum = 0
#     x = 0
#     while x < len(numbers):
#         sum += numbers[x]
#         x += 1
#     return sum
# total = sum_list([8, 2, 6, -5, 20, -9])
# print(total)

#13)
# def find_max(numbers):
#     x = 1
#     max = numbers[0]
#     while x < len(numbers):
#         if max > numbers[x]:
#             max = max
#         else:
#             max = numbers[x]
#         x += 1
#     return max
# highest = find_max([5, 8, 6, 9, 12, 1])
# print(highest)

#14)
# def reverse_list(numbers):
#     x = len(numbers) - 1
#     reversed = []
#     while x >= 0:
#         reversed.append(numbers[x])
#         x -= 1
#     return reversed 
# reverse = reverse_list([8, 5, 2, 6])
# print(reverse)

#15)
def no_duplicate(numbers):
    remove = []
    x = 0
    while x < len(numbers):
       y = 0
       origin = True
       while y < x:
            
            if numbers[x] == numbers[y]:
               origin = False
               break
            y += 1
       if origin == True:
            remove.append(numbers[x])
       x += 1           
    return remove
remove_duplicate = no_duplicate([8, 5, 9, 6, 8, 1, 6])
print(remove_duplicate)








