import random

choices = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0
playing = True

while playing:
    print("\nLet's play rock, paper, or scissors!")
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("\nChoose rock, paper, or scissors: ").lower()

    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}")

    # Menentukan pemenang
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        winner = "Player"
    elif player == computer:
        winner = "Tie"
    else:
        winner = "Computer"

    # Meningkatkan skor berdasarkan pemenang
    if winner == "Player":
        player_wins += 1
        print("You Won!")
    elif winner == "Computer":
        computer_wins += 1
        print("Computer Won!")
    else:
        print("It's a tie!")

    # Menampilkan skor terkini
    print(f"Current Score: Player - {player_wins} : Computer - {computer_wins}")

    # Meminta input apakah ingin bermain lagi
    play_again = input("\nPlay Again? (y/n): ").lower()
    if play_again != "y":
        playing = False

# Menampilkan skor final setelah permainan selesai
print(f"\nFinal Score: Player - {player_wins} : Computer - {computer_wins}")
if player_wins > computer_wins:
    print("Congratulations! You are the overall winner!")
elif computer_wins > player_wins:
    print("The computer is the overall winner!")
else:
    print("It's a tie overall!")

print("Thanks for playing! :D")

  