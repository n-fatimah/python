# words = ["apple", "banana", "cherry"]
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)


# original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# filtered_dict = {key: value for key, value in original_dict.items() if value > 2}
# print(filtered_dict)


dict = {'n': 'noor', 'b': 'bat', 'c': 'cat'}
dict_upper = {key: value.upper() for key, value in dict.items()}
print(dict_upper)

dict_plural = {key: value + 's' for key, value in dict.items()}
print(dict_plural)