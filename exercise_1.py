#5.1. More on Lists
# 1_ex
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()

#5.1.1. Using Lists as Stacks
# 2_ex 
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack

#5.1.2. Using Lists as Queues
# 3_ex
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival

#idomu ar main sitas pasirasys