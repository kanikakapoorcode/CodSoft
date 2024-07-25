print("------------------------------------------------------------------")
print("\n--------------Welcome ! to the rock and Scissors Game-------------")
print("\n------------------------------------------------------------------")
import random

def game():
    while True :
          user = input("Enter a Choice(rock , paper , scissors): ").lower()
          
          while user not in ["rock","paper","scissors"]:
              user = input("Invalid input . Please enter rock , paper or scissors : ").lower()
          
          possible_choices = ["rock","paper","scissors"]
          computer = random.choice(possible_choices)
          print(f"\nYou chose {user} , computer choses {computer}.\n")
          
          
          
          if user == computer :
              print(f"Both players Selected {user}. It's a tie !") 
          elif user == "rock" :
              if computer == "scissors":
                  print("Rock smashes scissors ! You win !")
              else:
                  print("Paper covers rock ! You lose !")
          elif user == "paper" :
              if computer == "rock":
                  print("Paper covers rock ! You win !")
              else:
                  print("Scissors cuts paper ! You lose !")
          elif user == "scissors" :
              if computer == "paper":
                  print("Scissors cuts paper ! You win !")
              else :
                  print("Rock smashes scissors ! You lose !")
                  
                  
                  
                  
          play_again = input("\n\nDo you want to play again ? (yes/no) : ").lower()
          while play_again not in ["yes","no"] :
              play_again = input("Invalid input . Please enter yes or no : ").lower()
          if play_again == "no":
              break
 
 
if __name__ == "__main__" :
    game()
    
                  