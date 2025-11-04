def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

details = {}
n = int(input("how many details do you want to enter?"))

for i in range(n):
    key = input("enter field name here(e.g.,name,age city)")
    value = input("enter field value here(e.g.,name,age city)")
    details[key] = value

show_details(**details)
