

names = ["Anna", "Tom", "Anna", "Lucas", "Tom"]
filtred_names = set(names)

a = "developpeur"
b = "personnalité"

first_word = set(a)
second_word = set(b)

same_letters = first_word & second_word

letters_in_first_word = first_word - second_word
letters_in_second_word =  second_word - first_word

user1 = {"cinéma", "musique", "sport"}
user2 = {"peinture", "musique", "yoga"}

def has_common_hobbies(user1, user2):
    return bool(user1 & user2)


dev1 = {"python", "git", "sql"}
dev2 = {"python", "docker", "linux"}

def compare_skills(dev1, dev2):
    same_skills = dev1 & dev2
    first_dev_skills = dev1 - dev2
    second_dev_skills = dev2 - dev1
    return f"Same skills : {same_skills}\nfirst dev skills : {first_dev_skills}\nsecond dev skills : {second_dev_skills}"


