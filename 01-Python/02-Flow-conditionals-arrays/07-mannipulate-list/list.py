

students = ["Alice", "Bob", "Charlie", "Diana", "Eva"]
filtred_students = students[2::-1]

scores = [12, 18, 15, 9, 20]
for i in range(len(scores)):
    if scores[i] < 15:
        scores[i] = 'FAIL'

letters = ['a', 'b', 'c', 'd', 'e', 'f']
filtred_letters = letters[0:3]
for i in range(len(filtred_letters)):
    filtred_letters[i] = filtred_letters[i].upper()

nums = [4, 7, 10, 5, 3, 8, 2, 6]
even_nums = []
for n in nums:
    if n % 2 == 0:
        even_nums.append(n)
print(min(even_nums))

data = [1, 2, 3, 4, 5, 6, 7, 8]
filtred_data = data[::-1]
filtred_data = [i for i in filtred_data if i > 4]


sorted(list(set('developpeur')))
