
#1) for x in range (50, 0, -1):
#     print(x)



#2) for x in range (50, 9, -1): 
#         print(x)


#3) for x in range (1, 101):
#     if x % 2 == 0:
#         print(x)


#4)n = int(input('Choose a number and ill tell you the sum of all numbers leading to it: '))
# total = 0
# for x in range(1, n+1):
#     total = total + x
# print(total)

#5)
# number = int(input('Choose a number and ill tell you its multiplication table:'))
# for x in range(1,11):
#     result = x * number
#     print(f"{number} * {x} = {result}")

#6)
# word = input('Enter the word "Python": ')
# while word != 'Python':
#       word = input('write it correctly as stated!: ')
# print ('good job!!')

#7)
# word = input('Enter a RANDOM word!: ')
# for x in range (0, len(word)):
#     C = word[x]
#     print(C)

#8)
# word = input('Enter a RANDOM word!: ')
# count = 0
# for c in word:
#     count += 1
# print('number of characters is: ', count)

#9)
# number = int(input('Enter a number (0 to stop): '))
# total = 0
# while number != 0:
#     total += number
#     number = int(input('Enter a number (0 to stop): '))
# print('your total is : ', total)

#10)
# number = int(input("Enter a number and i'll give you it's factorial: "))
# x = number
# total = 1
# for x in range(number, 1, -1):
#     total *= x
# print('your total is : ', total)

#11)
# number = int(input("Enter a number and i'll reverse it for you: "))
# c = number // 10
# reverse_count = number % 10
# while c != 0:
#     print(reverse_count, end="")
#     reverse_count = c % 10
#     c = c // 10
# print(reverse_count)

#12)
# number = int(input("Enter a number and i'll tell you if it's prime or not: "))
# is_prime = True
# for x in range (2, number):
#     division = number % x
#     if division == 0:
#         is_prime = False
#         break
# if is_prime == False:
#     print('is not prime')
# else :
#     print('is prime')

#13)
# number = int(input('Give me a number and ill give you its fibunnaci sequence: '))
# previous_number_sum = 0
# current_number_sum = 1
# for x in range (0, number):
#     print(previous_number_sum, end=" ")
#     S = previous_number_sum + current_number_sum
#     previous_number_sum = current_number_sum
#     current_number_sum = S

#14)
# number = int(input('Enter a number and ill give you its multiplication table in odd numbers only: '))
# x = 1
# while x <= 12:
#     if x % 2 != 0:
#         result = number * x
#         print(f"{number} * {x} = {result}")
#     x += 1

#15)
# word = input('give me a word and ill tell you how many vowels in it :')
# count = 0
# for x in range (0, len(word)):
#     c = word[x]
#     if c.lower() in 'eaiou':
#         count += 1
# print(count)

# printing asterisks in a piramid shape
# rows = 5
# x = 1
# while x <= rows:
#     y = 1
#     while y <= (rows - x):
#         print(" ", end="")
#         y += 1
#     z = 1
#     while z <= (2*x -1):
#         print("*", end="")
#         z += 1
#     print()
#     x += 1
    


    




    
    


