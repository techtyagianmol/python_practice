name = input("Enter your name:-")

def greet(name = "monty"):

    return f"hello {name}!"

if name.strip() == "":
    result = greet()
else:
    result = greet(name)

print(result)
