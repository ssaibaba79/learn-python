names = ["John","Stacy","Ian","Shan"]
messages = ["Hello","Hey","Welcome","Hi"]
print(names)

message = f"{messages[0]} {names[0].title()}"
print(message)
message = f"{messages[1]} {names[1].title()}"
print(message)
message = f"{messages[2]} {names[2].title()}"
print(message)
message = f"{messages[3]} {names[3].title()}"
print(message)

# add item to the end of the list
names.append("Poorni")

# insert item at an given position
names.insert(0,"Anicha")
names.insert(1,"Sashti")
print(names)

# prints as sorted, but the order on the list is
# not sorted.
print(sorted(names))
print(sorted(names, reverse=True))
print(names)

# reverse the order of items in a list
names.reverse()
print(names)

# sorts the items in ascending order
names.sort()
print(names)

# pop last element off the list
print(names.pop())
print(names)
# pop element at a givenindex
print(names.pop(1))
print(names)
print(names.pop(0))
print(names)
del names[2]
print(names)
# sorts the items in descending order
names.sort(reverse=True)
# remove by value
names.remove("Shan")
print(names)

# number of items in the list
print(len(names))

# prints the last items from list
print(names[-1])

# Throws IndexError as the list is empty
# errors =[]
# print(errors[-1])
