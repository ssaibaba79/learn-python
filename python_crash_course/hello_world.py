first_name  = " saravanan"
last_name = "SAibaba "

# Basics

full_name = f"{first_name.lstrip().title()} {last_name.rstrip().title()}"
gender = " male".strip().upper()
print(gender)

message = f"Hello [{full_name}] \n"
message += "Welcome to the world of Python!"
print(message)

url = "https://www.google.com"
url =url.removeprefix("https://")

# Comment goes here
file_name = "greeting.txt"
file_name = file_name.removesuffix(".txt")
print(f"File {file_name} is downloaded from {url}")