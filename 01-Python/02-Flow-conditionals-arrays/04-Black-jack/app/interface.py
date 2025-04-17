from black_jack import *

def interface():

    bank_score = pick_bank_score()
    player_score = 0

    while True:
        print("Card? 'y' or 'yes' to get a new card")
        player_response = input()
        if player_response == "y" or player_response == "yes":
            player_score += pick_player_card()
            print(state_of_the_game(bank_score, player_score))
            if player_score > 21 or player_score == 21:
                print(end_game_message(player_score, bank_score))
                break
        else:
            print(end_game_message(player_score, bank_score))
            break


interface()
