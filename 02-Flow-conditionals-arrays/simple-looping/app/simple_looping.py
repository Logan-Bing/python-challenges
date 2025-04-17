import random

def count_vowels(word: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    count = 0
    for letter in word:
        if letter in vowels:
            count += 1

    return count % 2 == 0

print(count_vowels("bonjour"))


def filter_special_words(words: list[str]) -> list[str]:

    filtered_words = []
    for word in words:
        if len(word) > 5 and count_vowels(word):
            filtered_words.append(word)

    return filtered_words

print(filter_special_words(["bonjour", "ami", "developpeur", "python", "loop", "voiture", "yeux","bonbon"]))

def find_multiple(a: int, b: int) -> int:

    n = 1

    while n % a != 0 or n % b != 0:
        n += 1

    return n

print(find_multiple(3, 5))


def greatest_common_divisor(a: int, b: int) -> int:

    d = min(a, b)

    while d > 0:
        if a % d == 0 and b % d == 0:
            return d
        d -= 1

print(greatest_common_divisor(18, 12))


def find_random_number():
    win_number = random.randint(1, 100)
    player_num = None

    while player_num != win_number:
        player_num = int(input("Deviner le nombre :"))
        if player_num < win_number:
            print("too Low")
        elif player_num > win_number:
            print("too High")
        else:
            print("You win")

find_random_number()
