# #5.1. More on Lists
# # 1_ex count,index,reverse,append,sort,pop
# def main():
#  fruits = ["apple","banana","kiwi","orange","orange","apple","pear"]
#  number_of_fruits = fruits.count("apple")
#  print(fruits.index("banana"))
#  print(number_of_fruits)
#  fruits.insert(2,"insertinam")
#  print(fruits)
#  fruits.reverse()
#  print(fruits)
#  fruits.append("kiwi")
#  print(fruits)
#  fruits_copy = fruits.copy()
#  print(fruits_copy)
#  fruits.sort()
#  print(fruits)
#  fruits.pop()
#  print(fruits)

# 5.1.1. Using Lists as Stacks
# 2_ex 
# stack = [3, 4, 5]
# stack.append("9")
# stack.append("10")
# stack.append("11")
# stack.pop()
# print(stack)


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

# for i in range(10):
#  squares.append[i**2]

# print(squares)

#Lambda function def
# numbers = [x+1 for x in range(10)]
# print(numbers)

# even_numbers = [num for num in range(10)]
# print(even_numbers)

"""
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
Only accept items that are "apple":
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]



# get all even numbers from 1-50

# numbers = [x for x in range(1,51) if x%2 == 0] 
# print(numbers)

###
# options = ["any", "albany", "apple", "world", "hello", ""]

# new_options = [word for word in options if word.startswith('a') and word.endswith('y')]
# print(new_options)

### # Flattening a matrix (list of lists)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flat_matrix = [num for row in matrix for num in row]

#### Categorize numbers as even or odd IF ELSE IN A COMPREHENSION
# numbers = [x for x in range(1,10)]

# new_categorie = ["Even" if x%2 == 0 else "Odd" for x in numbers]
# print(new_categorie)

##### List comp with functions
# def square(x):
#  return x**2

# squared_numbers = [square(x) for x in range(10)]
# print(squared_numbers)

### DICT COMPREHENSION
# # Creating a dictionary
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# my_dict = {k: v for k, v in pairs}
# print(my_dict)


### SET COMPREHENSION
# # Removing duplicates from a list while applying a function
# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# unique_squares = {x**2 for x in nums}
# print(unique_squares)



#
# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# new_list = [x**2 for x in vec]

# # filter the list to exclude negative numbers
# new_list_2 = [x for x in new_list if x>= 0]

# # apply a function to all the elements
# new_list_3 = [abs(x) for x in vec]
# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# cleaned_list = [x.strip() for x in freshfruit]

# # create a list of 2-tuples like (number, square)
# new_list_4 = [(x, x**2) for x in range(1,6)]

# # flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# flatten = [num for row in vec for num in row]
# print(flatten)



# ## GOOD PRACTICE
# number: int = '10'

# def upper_everything(elements: list[str]) -> list[str]:
#  return [element.upper() for element in elements]



### NESTED LIST COMPREHENSION
# if __name__ == "__main__":
#  main()