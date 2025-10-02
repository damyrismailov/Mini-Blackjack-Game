import random
import art
game_start = input("Do you want to play a Blackjack? (y/n)\n").lower()
if game_start == "y":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(art.logo)
    first_card = random.choice(cards)
    second_card = random.choice(cards)
    yes = random.choice(cards)
    yes_1 = random.choice(cards)
def blackjack():
    game_end = True
    while game_end:
             your_cards = []
             first_choice = 0
             final_you = first_card + second_card
             your_cards.append(first_card)
             your_cards.append(second_card)
             print(f"Your cards: , {your_cards}, your score is : {final_you}")
             yours = list(your_cards)

             computer_cards = []
             computer_score = yes + yes_1
             computer_cards.append(yes)
             computer_cards.append(yes_1)
             print(f"Computer card is [{yes}]")
             if computer_score < 17:
               #while computer_score < 17:
                computer_cards += str(random.choice(cards))
             if final_you == 21:
                 print("Blackjack!, You won! ")
                 return
             hit_or_stand = input("'Hit' or 'Stand'\n").lower()
             if hit_or_stand == "hit":
                hit = random.choice(cards)
                your_cards.append(hit)
                gg = int(your_cards)
                new_score1 = final_you + hit
                print(f"Your cards are {your_cards} score is: {new_score1}")
             if your_cards > 21:
                 print("You lost!")
                 return
             if hit_or_stand == "stand":
                 print(f"Dealers cards are [{yes},{yes_1} score is:{computer_score} ")
                 if final_you > 21:
                     print("You Busted!")
                     return
                 if  new_score1 > computer_score:
                     print("You won!")
                 if your_cards == 21:
                     print("Blackjack!")
                 if new_score1 < computer_score:
                  print("Dealer wins!")
                  return

blackjack()
