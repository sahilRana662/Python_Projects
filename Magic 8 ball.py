#  The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.#
import random
name = input("What is your name? ")
question = input("What is your question? ")
answer = ""
random_number = random.randint(1,9)

#rint(random_number)
if(random_number == 1):
  answer = "Yes-definetely"
elif random_number == 2:
  answer = "It is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My source say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
  

if question == "" and name == "":
    print("Please ask the  question!")
elif name == "" and question != "":
     print( "question :" + question)
elif name != "" and question != "":
    print(name + " asks: " + question)
else :
    print("Please " + name + " ask the question!")


if (question != "" and name != "") or (question != "" and name == "") :
 print("Magic 8-Ball's answer: " + answer)
else:
    print("Try again")