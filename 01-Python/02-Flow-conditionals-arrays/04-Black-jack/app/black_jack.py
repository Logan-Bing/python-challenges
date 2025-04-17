import random


def pick_bank_score():
    # Implémenter le score du croupier entre  16 et 21
    bank_score = random.randint(16, 21)
    return bank_score


def pick_player_card():
    player_score = random.randint(1, 11)
    return player_score


def state_of_the_game(bank_score, player_score):
    # Crée un message avec les scores => Your score is {score_player}, bank is {bank_score}
    return f"Your score is {player_score}, bank is {bank_score}"


def end_game_message(player_score, bank_score):

     if player_score > bank_score and player_score < 21:
         return "You beat the bank! You win."
     elif player_score == 21:
         return "Black JACK !!!! You win"
     elif player_score == bank_score:
         return "Tie. Replay the game"
     elif player_score < bank_score:
         return "You lose"
     else:
         return "You lose"
