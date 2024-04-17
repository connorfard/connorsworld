import random
import datetime

def run():
    counter = 0
    start = datetime.datetime.now()
    for x in range(int(questions)):
        number1 = random.randint(2,9)
        number2 = random.randint(2,9)
        question = input(f'''#{x + 1}: What is ''' + str(number1) + "x" + str(number2) + "? \n")
        answer = number1*number2
        #print('answer' + str(answer))
        if question == str(answer):
            print("correct")
            counter += 1
            print("you have 1 added to your score so you have " + str(counter))
        else:
            print("wrong")
            print("you still have " + str(counter))
    end = datetime.datetime.now()
    totaltime = end - start
    print(f"your total time was {totaltime}")
    return counter, totaltime


if __name__ == '__main__':
    print("welcome to the math quiz")
    players = input("How many people do you want to play with (press enter for 1?")
    if players == "":
        players = 1
    questions = input("How many questions do you want to do (press enter for 10)? \n")
    if questions == "":
        questions = 10
    scores = []
    for x in range(int(players)):
        score, totaltime = run()
        print(f"""You scored {score} points! You took {totaltime} seconds""")
        scores.append({"player": x, "score": score, "totaltime": totaltime})
    print(f "Final Scores: {scores}")
    # print("Player " + str(scores.index(max(scores))+1) + " won the game!")