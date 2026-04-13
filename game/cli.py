from Game import Game

def play_game():
    game=Game()

    human=game.human
    pc=game.pc

    game.turn=human

    human_amount=human.place_initial_bet()
    human.update_amount_bet(human_amount)

    pc_amount=pc.auto_match_or_raise(human_amount)
    pc_amount.update_amount_bet(human_amount)

    if pc_amount=="1":
        print("Towel throwin Human won")
        return

    game.turn=human
    game.pot=pc_amount+human_amount

play_game()
