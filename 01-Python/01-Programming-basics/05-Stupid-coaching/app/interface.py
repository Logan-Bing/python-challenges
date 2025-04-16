from stupid_coaching import coach_answer_enhanced

def interface():
    while True:
        user_input = input("You: ").strip()
        response = coach_answer_enhanced(user_input)
        print("Coach:", response)

        if user_input.strip() in ["I am going to work right now!", "I AM GOING TO WORK RIGHT NOW!"]:
            break

if __name__ == "__main__":
    interface()
