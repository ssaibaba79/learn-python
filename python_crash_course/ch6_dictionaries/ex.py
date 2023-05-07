question = {"prompt":"How much is 10 +5",
"answer_options" :[12, 15, 17, 19],
"current_answer_index" : 2,
}

print(question)

for k, v in question.items():
  print(k, v)

for k in question.keys():
  print(k, question.get(k))


x = 0
x1 = 1
n = 100

f = 0
print(f"{x}, {x1}")
while f < n:
  f = x + x1
  print(f);
  x = x1
  x1 = f


  