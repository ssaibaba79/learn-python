question = {"prompt":"How much is 10 + 5",
"answer_options" :[12, 15, 17, 19],
"current_answer":15,
}

while True:
  answer = input(f"{question['prompt']}\n{question['answer_options']}\n")
  print(answer)
  if answer != "":
    if int(answer) == question['current_answer']:
      print("Correct")
      break
    else:
      print("incorrect")
  else:
    print("Pl choose an answer from the options")
  print("try again")


