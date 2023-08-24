def anagram_checker(first_word, second_word):
    if len(first_word) == len(second_word):
        array_first_word = list(first_word)
        array_second_word = list(second_word)
        count = 0
        while count < len(first_word):
            if array_first_word[0] in array_second_word:
                array_second_word.remove(array_first_word[0])
                array_first_word.remove(array_first_word[0])
            count += 1
            if array_first_word == [] and array_second_word == []:
                print('It is an Anagram')
        else:
            print('Not an anagram')
    else:
        print('Not an anagram')


word1 = input('Enter first word: ')
word2 = input('Enter second word to compare: ')

anagram_checker(word1, word2)
