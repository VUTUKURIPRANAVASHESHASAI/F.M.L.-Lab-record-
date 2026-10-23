# ==============================================================================
# STRING PROGRAMS (1 to 5)
# ==============================================================================

# 1. Reverse a string
print("--- Program 1: Reverse a String ---")
text = "machinelearning"
reversed_text = text[::-1]
print(f"Original: {text} -> Reversed: {reversed_text}")
print()

# 2. Check whether a string is a palindrome
print("--- Program 2: String Palindrome Checker ---")
word = "radar"
is_pal = word == word[::-1]
print(f"Is '{word}' a palindrome? {is_pal}")
print()

# 3. Count vowels and consonants
print("--- Program 3: Count Vowels and Consonants ---")
sample_str = "hello environment"
vowels = "aeiouAEIOU"
v_count = sum(1 for char in sample_str if char in vowels)
c_count = sum(1 for char in sample_str if char.isalpha() and char not in vowels)
print(f"String: '{sample_str}' -> Vowels: {v_count}, Consonants: {c_count}")
print()

# 4. Count words in a sentence
print("--- Program 4: Count Words in a Sentence ---")
sentence = "Fundamentals of Machine Learning Lab practice questions"
word_count = len(sentence.split())
print(f"Sentence: '{sentence}'")
print(f"Word count: {word_count}")
print()

# 5. Find the frequency of each character
print("--- Program 5: Character Frequency Counter ---")
freq_str = "data"
freq_dict = {}
for char in freq_str:
    freq_dict[char] = freq_dict.get(char, 0) + 1
print(f"Character frequencies in '{freq_str}': {freq_dict}")
print()