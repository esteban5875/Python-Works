import time
import random

print("                     ")
print("=====================")
print("Rock, Paper, Scissors")
print("=====================")
print("You VS Me ! >:D")
print("=====================")
print("                     ")


while True:

    values = ["Rock", "Paper", "Scissors"]

    player = input(str("Enter your play, [Rock, Paper, Scissors] or 'Bye' to exit: "))

    invalid = "<Invalid> Input has to be lowercase or uppercase within: [Rock, Paper, Scissors, Bye]"



    def playit():
        return random.choice(values)

    def clock():
        return random.randint(1, 6)
        

    result = playit()
    play = player.lower()
    res = result.lower()
    time_result1 = clock()

    if play == "bye":
        break

    if play not in ["rock", "paper", "scissors", "bye"]:
        print("       ")
        print(invalid)
        print("       ")

    else:
        print("            ")
        print("Preparing...")
        print("            ")
        time.sleep(time_result1)
        print("           ")
        print("Deciding...")
        print("           ")
        time.sleep(time_result1)
        print("      ")
        print("My decision is...")
        print("                ")
        time.sleep(time_result1)
        print("=========")
        print(result)
        print("=========")
    
    if res == play:
        print("      ")
        print("=====================")
        print(f"{result.capitalize()} vs {player.capitalize()}")
        print("=====================")
        print("       ")
        print("======")
        print("Tie :|")
        print("======")
        print("      ")
    elif (res == "rock" and play == "paper") or (res == "scissors" and play == "rock") or (res == "paper" and play == "scissors"):
        print("       ")
        print("=====================")
        print(f"{result.capitalize()} vs {player.capitalize()}")
        print("=====================")
        print("       ")
        print("===========")
        print("You win :'(")
        print("===========")
        print("       ")
    elif (res == "paper" and play == "rock") or (res == "scissors" and play == "paper") or (res == "rock" and play == "scissors"):
        print("      ")
        print("=====================")
        print(f"{result.capitalize()} vs {player.capitalize()}")
        print("=====================")
        print("        ")
        print("============")
        print("You Lose >:D")
        print("============")
        print("        ")
    
