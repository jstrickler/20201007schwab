from ansi.color import fg, bg
from ansi.colour.fx import reset

prompt = fg.red("What is your name? ")

reply = input(prompt)

print(f"{fg.red('Hello')}, {fg.boldblue(reply)}")

