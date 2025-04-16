
def coach_answer(sentence):
    if sentence == "I am going to work right now!":
        return "Congratulations, have a great day!"
    elif sentence.endswith("?"):
        return "Silly question, get dressed and go to work!"
    else:
        return "I don't care, get dressed and go to work!"

def coach_answer_enhanced(sentence):
    cleaned = sentence.strip()

    if cleaned == "I AM GOING TO WORK RIGHT NOW!":
        return "Congratulations, have a great day!"

    if cleaned.isupper():
        return "I can feel your motivation! " + coach_answer(cleaned)

    return coach_answer(cleaned)
