print("welcome to quiz game")
score=0
playing=True
print("okay!,lets start the game:)")

while playing:
    questions=("who invented computer? ","what is a figure with eight sides called?","what is the third planet of our solar system called?","which organ purifies our blood?","which plant grows in desert?")
    answers=["charles babbage","octagon","earth","kidney","cactus"]
    for i in range(len(questions)):
        print(questions[i])
        user_answer=input("your answer:")
        if user_answer.lower()==answers[i].lower():
            print("correct")
            score=score+1
        else:
            print("incorrect")
    print("you have got "+str(score)+"questions correct")
    print("your final result is "+str(score))
    play_again=input("do you want to play again?(yes/no):")
    if play_again.lower()!="yes":
                playing=False

            




