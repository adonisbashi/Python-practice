# Ask user for their name
name = input("What's your name? ").strip().title()

# Split users name into first name and last name
first, last = name.split(" ")


# Say hello to the user
print(f"hello, {first}")