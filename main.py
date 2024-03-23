import random
import datetime
counter = 0
questions = input("How many questions do you want to do (press enter for 10)? \n")
if questions == "":
    questions = 10
start = datetime.datetime.now()
for x in range(int(questions)):
    number1 = random.randint(1,9)
    number2 = random.randint(1,9)
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
