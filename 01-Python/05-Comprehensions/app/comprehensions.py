
words = ["python", "api", "developpeur", "code", "ux"]
long_word_lengths = [len(word) for word in words if len(word) > 4]

vowels = "aeiou"
words = ["bonjour", "developpeur", "python"]
# count_vowels = {word:  for word in words}
# print(count_vowels)

words = ["bonjour", "developpeur", "python"]
unique_letter = [set(word) for word in words]


def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 4))

names = ["julia", "logan", "rudy", "alice", "tom"]

filtred_names = []
for name in names:
    if len(name) > 4:
        filtred_names.append(name)

print(filtred_names)

filtred_names_best = [name for name in names if len(name) > 4]
print(filtred_names_best)
