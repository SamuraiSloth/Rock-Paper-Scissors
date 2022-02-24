import random

#variables
play = ""
bot = ""
score1 = 0
score2 = 0
possible = ["rock", "paper", "scissors"]
#replay = "y"

#while replay == "y":
#Chooses your and the bots actions
play = input("Rock, paper, or scissors? ")
bot = possible[random.randint(0, 2)]

#If you win
if play == "rock" and bot == "scissors" or play == "paper" and bot == "rock" or play == "scissors" and bot == "paper":
  score1 += 1
  print("Bot played " + bot)
  print("Congratulations, you won!")
  print("You: " + str(score1))
  print("Computer: " + str(score2))
  #reply = input("would you like to play again?: ")
  
  #If you lose
if bot == "rock" and play == "scissors" or bot == "paper" and play == "rock" or bot == "scissors" and play == "paper":
  score2 += 1
  print("Bot played " + bot)
  print("Sorry, you lost :(")
  print("You: " + str(score1))
  print("Computer: " + str(score2))
  #reply = input("would you like to play again?: ")

#If you tie
if bot == play:
  print("It's a tie!")
  print("You: " + str(score1))
  print("Computer: " + str(score2))
