import anagram


def is_palindrome(word):
    list1 = list(word.lower())
    list2 = list(word.lower())
    list2.reverse()
    return list1 == list2


print(is_palindrome('Racecar'))
print(is_palindrome('hello'))
print(anagram.are_anagrams('argentino', 'ignorante'))
