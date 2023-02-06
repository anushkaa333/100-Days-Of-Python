import random

print("Snake Water Gun Game")
print("User will be given 5 chances")

def game(user_score, comp_score):
    for i in range(5):
        user = int(input("1 for snake\n 2 for water\n 3 for gun\n"))
        print("User input", user)
        comp = random.randint(1,3)
        print("Comp input", comp)
        if(user == comp):
            print("No point")
        elif(user == 1 and comp == 2):
            user_score = user_score + 1
        elif(user == 1 and comp == 3):
            comp_score = comp_score + 1
        elif(user == 2 and comp == 1):
            comp_score = comp_score + 1
        elif(user == 2 and comp == 3):
            user_score = user_score + 1
        elif(user == 3 and comp == 2):
            comp_score = comp_score + 1
        elif(user == 3 and comp == 1):
            user_score = user_score + 1
        else:
            print("Invalid Syntax")
        
        print("U Score", user_score)
        print("C Score", comp_score)

    return "User is winner" if user_score>comp_score else "Comp is winner"



ans = game(0, 0)
print(ans)