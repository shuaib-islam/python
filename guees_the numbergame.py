import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is no current high score")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
        
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hey there!YOU ARE NOW IN MY DOMAIN!")
    player_name = input("Enter your name!")
    wanna_play = input("YOU SHALL PLAY A GAME OF NUMBER GUESSING🗿(Make a chocie YES/NO)").format(player_name)
    
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            
            guess = input("Pick a number from 1 to 10")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("GUESS A NUMBER WITHIN THE RANGE")
            if int(guess) == random_number:
                print("YOU...you got it right?")
                attempts += 1
                attempts_list.append(attempts)
                print("it took you { attempts}".format(attempts))
                play_again = input("Would you like to risk your life for 5 bucks again?")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "No" :
                    print("I finally get to go home early.")
                    break
                elif int(guess) < random_number:
                    print("It's lower")
                    attempts += 1
                elif int(guess) > random_number:
                    print("Its higher")
                    attempts += 1
        except ValueError as err:
            print("Oh that is not a valid value, TRY AGAIN!!!")
            print("({})".format(err))
            
        else:
            print("Thats ok, have a nice day")
    if __name__ == '__main__':
        start_game()
