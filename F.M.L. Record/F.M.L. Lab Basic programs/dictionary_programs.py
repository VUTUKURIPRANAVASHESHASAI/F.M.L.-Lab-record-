# ==============================================================================
# DICTIONARY PROGRAMS (1 to 5)
# ==============================================================================

# 1. Create a student dictionary
print("--- Program 1: Create Student Dictionary ---")
student = {
    "name": "Arjun",
    "roll_no": "ML042",
    "grade": "A",
    "subject": "Machine Learning"
}
print(f"Student details dictionary: {student}")
print()

# 2. Count word frequency
print("--- Program 2: Count Word Frequency ---")
text_block = "apple banana apple cherry banana apple"
words = text_block.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print(f"Text: '{text_block}' -> Word frequency: {word_freq}")
print()

# 3. Merge two dictionaries
print("--- Program 3: Merge Two Dictionaries ---")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# Merging dict2 into dict1 (Python 3.9+)
merged_dict = dict1 | dict2
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")
print(f"Merged Dictionary: {merged_dict}")
print()

# 4. Find the key with the maximum value
print("--- Program 4: Find Key with Maximum Value ---")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
max_key = max(scores, key=scores.get)
print(f"Scores directory: {scores} -> Key with max value: '{max_key}' (Value: {scores[max_key]})")
print()

# 5. Sort a dictionary by values
print("--- Program 5: Sort a Dictionary by Values ---")
unsorted_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print(f"Original: {unsorted_dict} -> Sorted by values: {sorted_dict}")
print()