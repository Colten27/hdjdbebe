import random

Choices = ["rock", "paper", "sissors"]
Choose = random.choice(Choices)

user = input ("Welcome to rock paper sissors, choose rock paper or sissors!")
if Choose == "rock":
    print ("The computer choose rock")
elif Choose == "paper":
    print ("The computer choose paper")
elif Choose == "sissors":
    print ("The computer choose sissors")

if user == "rock" and Choose == "rock":
    print ("You Tied")
elif user == "paper" and Choose == "paper":
    print ("You Tied")    
elif user == "sissors" and Choose == "sissors":
    print ("You Tied")   
elif user == "rock" and Choose == "sissors":
    print ("You Won")   
elif user == "paper" and Choose == "rock":
    print ("You Won")
elif user == " paper" and Choose == "rock":
    print ("You Won")
elif user == "rock" and Choose == "paper":
    print ("You Lose")  
elif user == "sissors" and Choose == "rock":
    print ("You Lose") 
elif user == "paper" and Choose == "sissors":
    print ("You Lose")