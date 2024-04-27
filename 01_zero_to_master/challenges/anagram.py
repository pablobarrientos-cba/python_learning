def are_anagrams(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    blank_space = ' '

    set1.remove(blank_space) if blank_space in set1 else set1
    set2.remove(blank_space) if blank_space in set2 else set2

    return set1 == set2


print(are_anagrams('a dirty room ', 'dormitorya'))
print(are_anagrams('hello', 'world'))
