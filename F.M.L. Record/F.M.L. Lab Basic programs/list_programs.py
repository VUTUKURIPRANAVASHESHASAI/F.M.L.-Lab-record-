# ==============================================================================
# LIST PROGRAMS (1 to 5)
# ==============================================================================

# 1. Find the largest element in a list
print("--- Program 1: Largest Element in a List ---")
nums = [12, 45, 2, 89, 34, 11]
largest = max(nums)
print(f"List: {nums} -> Largest: {largest}")
print()

# 2. Find the smallest element
print("--- Program 2: Smallest Element in a List ---")
smallest = min(nums)
print(f"List: {nums} -> Smallest: {smallest}")
print()

# 3. Sort a list
print("--- Program 3: Sort a List ---")
unsorted_list = [40, 10, 50, 20, 30]
sorted_list = sorted(unsorted_list)
print(f"Original: {unsorted_list} -> Sorted: {sorted_list}")
print()

# 4. Remove duplicate elements
print("--- Program 4: Remove Duplicate Elements ---")
dup_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = list(set(dup_list))
print(f"With duplicates: {dup_list} -> Unique elements: {unique_list}")
print()

# 5. Find the second largest number
print("--- Program 5: Second Largest Number ---")
sample_list = [10, 20, 4, 45, 99, 99, 45]
# Remove duplicates first to ensure accuracy
unique_sorted = sorted(list(set(sample_list)))
if len(unique_sorted) >= 2:
    second_largest = unique_sorted[-2]
    print(f"List: {sample_list} -> Second largest: {second_largest}")
else:
    print(f"List: {sample_list} -> Not enough unique elements")
print()