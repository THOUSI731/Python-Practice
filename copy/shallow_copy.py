import copy

original_list = [1, 2, 3, 4, 5, 6]
deep_copy = copy.deepcopy(original_list)

# Modifying an element in the deep copy
deep_copy[0] = 100

print(original_list)  # Output: [[1, 2, 3], [4, 5, 6]]
