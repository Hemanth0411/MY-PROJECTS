import requests as r
import json
import random

user_score = 0
total=0
game = True

print("Welcome to quiz game!!")
input("Press enter to continue...")

while game:
  quiz = r.get("https://opentdb.com/api.php?amount=1")

  if(quiz.status_code)!=200:
    print('Sorry there was a problem retrieving the question. Please enter to try again or quit.')
  else:
    qn = json.loads(quiz.text)
    qn1 = qn['results'][0]['question']
    
    print(f"\n"+qn1.replace("&quot;", "'"))
    
    options = qn['results'][0]['incorrect_answers']
    correct_opt = qn['results'][0]['correct_answer']
    options.append(correct_opt)
    random.shuffle(options)
    
    for i  in range(len(options)):
      print(str(i+1)+") "+options[i])
    user_answer = input("Your Answer: ").lower()
    total+=1
    
    if user_answer == correct_opt.lower():
      user_score+=1
      print("Your answer is correct.")
    else:
      print("Wrong. The correct answer is {}".format(correct_opt))
    
    print(f"Your score is {user_score}/{total}")
    choice = input("Would you like to try again?(Y/N): ").lower()
    
    if choice == 'y':
      continue
    break  
print("Thanks for playing!!")

