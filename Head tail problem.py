import random


try:
    coin = ['H', 'T']
    number_of_game = int(input("Enter Number of Game you want to play: "))
    pay = float(input("How much Money You want to spend per chance : "))
    win = 0
    lost = 0
    for i in range(1, number_of_game + 1):
        R = input("Enter Your Chose : For Head 'H' or For Tail 'T'")
        if R == random.choice(coin):
            print("You are win ")
            win = win + 1
        else:
            print("You are lost")
            lost = lost + 1

    spendMone = number_of_game * pay
    print(f"You are win {win} times and lost {lost} times")
    print(f"You are pay in game {spendMone} dollar")
except:
    print("You are enter wrong Value ... please enter right one = ")
