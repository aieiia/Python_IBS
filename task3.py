# Set of numbers
numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

# Function which gets rid of all even numbers and the odd ones which are less than 50
def odd_num_filter(num):
# Condition to sort out the needed numbers
  if(num % 2) == 1 and num > 50:
    return True
  else:
    return False
# Output of the result (using list here to convert the filter object into Python List)
print(list(filter(odd_num_filter, numbers)))