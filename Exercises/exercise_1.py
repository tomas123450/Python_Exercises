
# list = []
# tuple = () tiesiog greitesnis uz list ir unchangable
# set = {} negali kartotis elementai, uordered
# dict = {key:value} pairs ordered and changable no duplicates alowed
# enumerate ismokt, zip, open

def printlabas():
 """
 prints labas
 """
 print("labas")

help(printlabas)
### DICT COMPREHENSION
# names = ["John","Tom","Bob"]
# surnames = ["Smith","Fenuci","Benuci"]
# print(list(zip(names,surnames)))
# name_surname = {name:surname for name,surname in zip(names,surnames)}
# print(name_surname)


#5.1.2. Using Lists as Queues
# 3_ex
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()            # The first to arrive now leaves

# queue.popleft()                 # The second to arrive now leaves

# print(queue)                           # Remaining queue in order of arrival


# 5.1.3. List Comprehensions
# squares = []
# """Create a list of the first letter of each word in a given list: - """
# words = ["apple", "banana", "cherry", "date"]

# """Create a list of the lengths of each word in a given sentence: NEZINAU split()"""
# sentence = "The quick brown fox jumps over the lazy dog"

# #Lambda function def
# squared = map(lambda x: x**2, [1,2,3])
# print(squared)


# #### Categorize numbers as even or odd IF ELSE IN A COMPREHENSION
# numbers = [x for x in range(1,10)]

# new_categorie = ["Even" if x%2 == 0 else "Odd" for x in numbers]
# divisible = [(x,"Divisible") if x%3 == 0 else (x,"Not divisible by 3")for x in numbers]
# print(divisible)


# ## DICT COMPREHENSION
# # Creating a dictionary
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# my_dict = {k:v for k,v in pairs}
# print(my_dict)


# ## SET COMPREHENSION
# # Removing duplicates from a list while applying a function
# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# unique_squares = {x**2 for x in nums}
# print(unique_squares)

# ## GOOD PRACTICE
# number: int = '10'


### NESTED LIST COMPREHENSION
# if __name__ == "__main__":
#  main()