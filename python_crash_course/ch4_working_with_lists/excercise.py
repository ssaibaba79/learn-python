# Chapter 4 : Working with lists

soccer_teams  = ["Arsenel","Manchester United","Chelsea","Liverpool","Real Madrid"]
hl = "------------------------------"
print("========= Soccer Teams =========")
for team in soccer_teams:
  print(f"{hl}\n{team}\n{hl}")
print("================================")

# Numerical lists
# range()

numbers = list(range(10))
print(numbers)
numbers = list(range(1,15))
print(numbers)
numbers = list(range(0, 16, 2))
print(numbers)

# squares
for number in range(1, 11):
  print(number ** 2)

# min, max and sum
odd_numbers = list(range(1, 100, 2))
print(odd_numbers)
print(sum(odd_numbers))
print(min(odd_numbers))
print(max(odd_numbers))

# list comprehension

squares = [value **2 for value in range(1,11)]
print(squares)

greets = ["Hello","Bonjour", "Vanakkam"," Konichiva","AnnYoung"]
names = ["Ann","Cole","Anicha","Mike","Maya"]

greetings =[f"{greets[i]} {names[i]}" for i in range(0,5)]
print(greetings)

# slice
print(greetings[0:3])
print(greetings[1:4])
print(greetings[-3:])
greetings_clone = greetings[:]

greetings_clone.append("Namaste")
print(greetings)
print(greetings_clone)

# Tuple - immutable list
directions = ("LEFT", "RIGHT", "UP", "DOWN","FORWARD", "BACKWARD")
for direction in directions:
  print(direction)

direction = "cross"
if direction not in directions:
  print(f"Direction {direction} is  not valid")

users = ["sal@g.com","penny@k.com", "jimmy@x.com"]
new_users = ["Jimmy@x.com","carol@x.com"]
for user in new_users:
  if user.lower() in users:
    print(f"User {user} already exists")
  else:
    print(f"User {user} is allowed")

alien_colors = ['red','green','blue']
alien_kill_counter = [0,0,0]

kill = 'red'
if kill.lower() == 'red':
  alien_kill_counter[0] += 1
elif kill.lower() == 'green':
  alien_kill_counter[1] += 1
elif kill.lower() =="blue":
  alien_kill_counter[2] += 1

print(f"Alien kills R:{alien_kill_counter[0]},G:{alien_kill_counter[1]},B:{alien_kill_counter[2]}")

