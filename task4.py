# Initial dictionary
dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

# Creating new dictionary
dict1 = {}
# Filling it with elements of the initial dictionary
for i in dict:
  # Condition to sort out the needed elements
  if dict[i] >= 3: dict1[dict[i]] = i

# Output of the result
print(dict1)