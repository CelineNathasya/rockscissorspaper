from random import randrange

def home():
    print("\nwelcome to batu gunting kertas game!")
    print("pick level")
    print("1. Easy")
    print("2. Impossible")
    print("3. Not going to play")
    print('')
    user_answer = int(input("pick: "))
    return user_answer

def choices(number):
    choice = ["batu", "gunting", "kertas"]
    player_choice = choice[number]
    return player_choice

def user_pick():
    user_choice = choices(int(input("pick \n 1. batu \n 2. gunting \n 3. kertas \n:")) - 1)
    return user_choice

def easy_comp_pick():
    random_pick = randrange(0,3)
    comp_choice = choices(random_pick)
    return comp_choice

def impossible_comp_pick():
    user = user_pick()
    if user == choices(0):
        comp = choices(2)
    elif user == choices(1):
        comp = choices(0)
    else : comp = choices(1)
    return user, comp


def logic(user, comp):
    if user == choices(0):
        if comp == choices(0):
            print("draw")
        elif comp == choices(1):
            print("win")
        else : print("lose")
    elif user == choices(1):
        if comp == choices(0):
            print("lose")
        elif comp == choices(1):
            print("draw")
        else : print("win")
    else :
        if comp == choices(0):
            print("win")
        elif comp == choices(1):
            print("lose")
        else : print("draw")

def easy_game():
    user = user_pick()
    comp = easy_comp_pick()
    print(user + " vs " + comp)
    logic(user, comp)

def impossible_game():
    user, comp = impossible_comp_pick()
    print(user + " vs " + comp)
    logic(user, comp)


if __name__ == "__main__":
    on = True
    while on == True:
        ans = home()
        if ans == 1 :
            easy_game()
        elif ans == 2 :
            impossible_game()
        else : on = False


