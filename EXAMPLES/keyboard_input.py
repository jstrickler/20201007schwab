
user_prompt = "What is your name: "
user_name = input(user_prompt)
quest = input("What is your quest? ")
print(f"{user_name} seeks {quest}")

raw_num = input("Enter number: ")  # input is always a string
num = float(raw_num)  # convert to numbers as needed

print(f"2 times {num} is {num * 2}")
