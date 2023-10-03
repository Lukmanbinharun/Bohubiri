from random import randint,randrange

low = 1
hi = 50

correct_answer = randrange(low,hi)
win = False


while(True):
    w = input("Do you went to play Game(Y/N):")
    if( w == 'Y'):
        for i in range(1,6):
            print(f"Your Chance No {i}.")
            user_ans = int(input("Enter any Number: "))
            print(user_ans)
            if( user_ans == correct_answer):
                print("You win")
                win = True
                break
            elif user_ans < correct_answer:
                print("Correct answer is greater!")
            else: print("Correct answer is smaller!")
    else: break


    if(not win):
        print("You loss!")






