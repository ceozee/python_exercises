def is_palindrome(word):
    print('True') if word == word[::-1] else print('False')


is_palindrome(input('Enter string: '))