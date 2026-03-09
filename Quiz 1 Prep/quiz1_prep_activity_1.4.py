# ST1 Quiz 1 Prep - Activity 4

# Write a program that asks the user to enter a sentence.
# The program should determine and print the following information: 
# The ﬁrst character in the string of text and the number of times it occurs in the string.
# The last character in the string of text and the number of times it occurs in the string.

sentence = input("Please enter a sentence: ")
sentence_lower = sentence.lower()
first_char = sentence_lower[0]
last_char = sentence_lower[-1]

print(f"There are {sentence_lower.count(first_char)} occurences of '{first_char}'"
      f"and {sentence_lower.count(last_char)} occurences of '{last_char}' in your sentence.")