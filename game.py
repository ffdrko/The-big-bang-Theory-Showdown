import random as r
print("Welcome to the Rock Paper Scissors Lizard Spock Game!")
print("Rock, Paper, Scissor, Lizard, Spock")
user_choice = input("What will you choose? ")

gamer_option = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
gamer_choice = r.choice(gamer_option)

if user_choice == "Rock" and gamer_choice == "Scissors":
    print(f"{user_choice} crushes {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Rock" and user_choice == "Scissors":
    print(f"{gamer_choice} crushes {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Spock" and gamer_choice == "Rock":
    print(f"{user_choice} vaporizes {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Spock" and user_choice == "Rock":
    print(f"{gamer_choice} vaporizes {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Paper" and gamer_choice == "Spock":
    print(f"{user_choice} disproves {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Paper" and user_choice == "Spock":
    print(f"{gamer_choice} disproves {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Lizard" and gamer_choice == "Paper":
    print(f"{user_choice} eats {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Lizard" and user_choice == "Paper":
    print(f"{gamer_choice} eats {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Scissors" and gamer_choice == "Lizard":
    print(f"{user_choice} decapitates {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Scissors" and user_choice == "Lizard":
    print(f"{gamer_choice} decapitates {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Spock" and gamer_choice == "Scissors":
    print(f"{user_choice} smashes {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Spock" and user_choice == "Scissors":
    print(f"{gamer_choice} smashes {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Lizard" and gamer_choice == "Spock":
    print(f"{user_choice} poisons {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Lizard" and user_choice == "Spock":
    print(f"{gamer_choice} poisons {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Rock" and gamer_choice == "Lizard":
    print(f"{user_choice} crushes {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Rock" and user_choice == "Lizard":
    print(f"{gamer_choice} crushes {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Paper" and gamer_choice == "Rock":
    print(f"{user_choice} covers {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Paper" and user_choice == "Rock":
    print(f"{gamer_choice} covers {user_choice}")
    print("Computer Win. :(")
elif user_choice == "Scissors" and gamer_choice == "Paper":
    print(f"{user_choice} cuts {gamer_choice}")
    print("You Win!!!")
elif gamer_choice == "Scissors" and user_choice == "Paper":
    print(f"{gamer_choice} cuts {user_choice}")
    print("Computer Win. :(")
elif user_choice == gamer_choice:
    print(f"{user_choice} and {gamer_choice},It's a draw")
else:
    print("Try to follow the game move please.")