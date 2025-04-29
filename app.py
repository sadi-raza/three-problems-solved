# ✅ Assignment 3: Problem-Solving Challenges
# 🔹 Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.
# Example:
# 🔹 Input: "hello"
# 🔹 Output: "olleh"
# 💡 Hint: Use Python's slicing feature.

# 🔹 Problem 2: Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
# Example:
# 🔹 Input: "Apple"
# 🔹 Output: 2
# 💡 Hint: Use a loop and check if each character is in a set of vowels.

# 🔹 Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns the sum of its digits.
# Example:
# 🔹 Input: 1234
# 🔹 Output: 10
# 💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.

# 🔹 Problem 1: Reverse a String
def reverse_string(s: str):
    
    return s[::-1]
result = reverse_string("hello") 

print(result) 


# 🔹 Problem 2: Count Vowels in a String

def count_vowels(s):
    vowels = {"a", "e", "i", "o", "u"}  # Set of vowels
    count = 0
    for char in s.lower():  # Convert to lowercase for case-insensitive check
        if char in vowels:
            count += 1
    return count

# Example usage:
result = count_vowels("Apple") 
print(result)  

# 🔹 Problem 3: Sum of Digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

result = sum_of_digits(1234)

print(result)  





