test = {
  "name":"Math Test 1",
 "questions": [
    { "prompt":"How much is 10 + 5",
      "answer_options" :[12, 15, 17, 19],
      "current_answer":15
    },
    { "prompt":"How much is 25 / 5",
      "answer_options" :[7, 5, 1, 3],
      "current_answer":5,
    }
  ]
}

## Play a question
def play_question(index, question, attempts = 3):
  while attempts > 0:
    answer = input(f"{index}.{question['prompt']}\n{question['answer_options']}\n")
    print(answer)
    if answer != "":
      if int(answer) == question['current_answer']:
        print("Correct")
        return
      else:
        print("incorrect")
    else:
      print("Pl choose an answer from the options")
    print("try again")
    attempts -= 1
  print(f"exhausted all attempts")

#Plays a test2

def play_test(test):
  print(f"Test : {test['name']}")
  i = 1
  for question in test['questions']:
    play_question(i, question)
    i +=1

play_test(test)
