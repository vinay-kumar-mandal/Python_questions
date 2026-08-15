# Take a character and determine whether it is a vowel, consonant, digit, or special character.
char = input("Enter a character: ")

if char in "aeiouAEIOU":
    print("The character is a vowel.")
elif char.isalpha():
    print("The character is a consonant.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")