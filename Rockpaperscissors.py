#import random allows me to use python's random function to select between rock, paper, and scissors
import random
import os
import sys
import subprocess

'''I'm setting a variable for what the computer and user choose so that I can use it for the different scenarios in rock, paper, scissors'''
user_choice = input("Enter a choice (rock, paper, or scissors):")
possible_choices = ["rock","paper","scissors"]
computer_choice = random.choice(possible_choices)

def rock_paper_scissors():
  #This is the scenario for a tie between the user and computer
  if user_choice == computer_choice:
    print("Both you and the computer chose {}. Its a tie".format(user_choice))

  #These are all the different scenarios for rock, paper, scissors. Since I already wrote the scenarios for a tie, it saves me time so I don't have to write out all the scenarios

  elif user_choice == "rock":
    if computer_choice == "paper":
      print("You lost. paper covers rock!")
    else:
      print("You won, rock smashes scissors!")

  elif user_choice == "paper":
    if computer_choice == "scissors":
      print("You lost, scissors cut paper.")
    else:
      print("You won, paper covers rock!")

  elif user_choice == "scissors":
    if computer_choice == "rock":
      print("You lost, rock smashes scissors")
    else:
      print("You won, scissors cuts paper!")

  play_again = input("Play again? y for yes n for no ")

  if play_again == "y":
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
  else:
    return

rock_paper_scissors()