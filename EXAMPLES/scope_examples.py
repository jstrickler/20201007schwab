
X = 42  # (file) global variable

def function_a(): # {
    y = 5  # local variable to function_a(), or nonlocal to function_b()
# }
    
def function_b():
    person = "Abe Lincoln"
    year = 1865
    print("bbbbbb")
    print("wahooooooo")



F = function_a()  # calling function_a, which returns function_b
F()  # calling function_b
