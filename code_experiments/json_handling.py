import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(f'{index+1}.{alternative}')
    user_choice = int(input('\nChoose the correct answer: '))
    print('\n')
    question["user_choice"] = user_choice
    
    print(f'Your answer: {question["user_choice"]}', \
          f'Correct answer: {question["correct_answer"]}\n')
    if user_choice == int(question['correct_answer']):
        score = score + 1

print(f'your score is:{score}/{len(data)}')




