# A list is an iterable, meaning we can get an iterator from it using the iter() function.
my_list = ['Jasmine', 'b', 'c', 'd', 'e']
iterator = iter(my_list)

# We can manually retrieve elements using the next() function.
print(next(iterator))  # Output: a
print(next(iterator))  # Output: b
print(next(iterator))  # Output: c

# You can keep calling next() until the iterator is exhausted.
# Uncomment the next line to raise StopIteration when the iterator is exhausted:
# print(next(iterator))  # Raises StopIteration

# 2. Using a for Loop with an Iterator

# Python automatically creates an iterator when using a for loop, so there's no need to manually call iter() and next().
print("\nUsing a for loop to iterate through the list:")
for item in my_list:
    print(item)
# Output:
# 10
# 20
# 30
# 40
# 50
