import random
game_list = ["Rock", "Paper", "Scissors"]

Bharatesh_choice = input("Choose Rock, Paper, or Scissors: ")

Computer_choice = random.choice(game_list)

print("Bharatesh: ", Bharatesh_choice)

print("Computer: ", Computer_choice)


if Bharatesh_choice == Computer_choice:

    print("It's a tie!")

elif Bharatesh_choice == "Rock" and Computer_choice == "Scissors":

    print("You win!")

elif Bharatesh_choice == "Paper" and Computer_choice == "Rock":

    print("You win!")

elif Bharatesh_choice == "Scissors" and Computer_choice == "Paper":

    print("You win!")

else:

    print("Computer wins!")