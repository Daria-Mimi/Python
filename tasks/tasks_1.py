def anagrams(word, words):
    if sorted(word) == sorted(words):
        return True
    else:
        return False

print(anagrams("abc", "cba"))