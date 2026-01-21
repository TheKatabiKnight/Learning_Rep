#📖 The Spellbook: Recursion


#⚔️ Training Grounds: The Descending Echo
# def echo_countdown(n):
#     if n == 0:
#         return
#     print(n)
#     echo_countdown(n - 1)
# echo_countdown(5)

# 📜 Legendary Tip: The Call Stack
# Grand Overseer, you have successfully managed the Call Stack. Every time your function calls itself, 
# Python places a 'Memory Plate' on a tall stack. If you forget your Base Case, 
# the stack grows until it hits the ceiling of the world, resulting in the dreaded RecursionError (Stack Overflow). 
# Always ensure your Base Case is the first thing you build!



#🌑 Training Grounds: The Depth Gauge
# def recursive_sum(n):
#     if n == 1:
#         return 1
#     return recursive_sum(n-1) + n
# print(recursive_sum(5))

# 📜 Legendary Tip: The Tail of the Echo
# Grand Overseer, your recursion is elegant. However, be mindful that Python has a limit on how deep these echoes can go
# (usually 1,000 calls). To survive deeper canyons, masters use Tail Call Optimization or iterative rituals, 
# but for the battles ahead, your current recursive steel is more than enough!


#Side Quest: The Ancestral Factorial
# def calculate_factorial(n):
#     if n == 0:
#         return 1   
#     return n * calculate_factorial(n-1)
# print(calculate_factorial(5))



# Main Quest: The Nested Vault Flattener
# def sum_nested_list(data):
#     total = 0
#     for num in data:
#         if type(num) == list:
#             total += sum_nested_list(num)   
#         else:
#             total += num
#     return total
# print(sum_nested_list([10, [20, 30], 40]))



#Legendary Quest: The Fibonacci Spiral
# def get_fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return get_fibonacci(n-1)+get_fibonacci(n-2)
# print(get_fibonacci(7))

# 📜 Legendary Tip: The Memory of the Echo
# Grand Overseer, your Fibonacci recursion was elegant, but it calculated the same branches many times 
# (e.g., calculating F(3) over and over). In higher-level sorcery, 
# we use Memoization—storing the results of our echoes in a dictionary so we never have to calculate the same depth twice. 
# It turns a spell that takes an age into one that finishes in a heartbeat!
