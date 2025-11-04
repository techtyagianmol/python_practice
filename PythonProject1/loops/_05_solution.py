# find the first non repeated character in the user_input_string;

input_str = input("Enter the string:-")

for char in input_str:
    if input_str.count(char) ==1:
        print("char is ", char)
        break

