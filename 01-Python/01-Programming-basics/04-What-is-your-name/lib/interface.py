from what_is_your_name import compute_name

def interface():
    first_name = input("Entrer votre prénom: ")
    middle_name = input("Entrer votre deuxiéme prénom: ")
    last_name = input("Entrer votre nom de famille: ")

    complete_name = compute_name(first_name, middle_name, last_name)
    len_name = len(complete_name)
    
    sentence = f"Hello {complete_name}, has got {len_name} characters, including spaces"
    return sentence

print(interface())
