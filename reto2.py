def is_palindrome(text):
    # Convert the text to lowercase and remove spaces
    text = text.lower().replace(" ", "")
    
    # Compare the text with its reverse
    if text == text[::-1]:
        return True
    else:
        return False

# Ask for user input
word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
