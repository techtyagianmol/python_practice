order_size = input("order_size->type->small,medium,large:-")

extra_shot = input("do you want exxtra_shot type-yes or no:-")

if extra_shot == "yes":
    coffee = order_size +", "+ "coffee with an extra shot"
elif extra_shot == "no":
    coffee = order_size +", "+ "coffee"
else:
    coffee = order_size +", " +"you doesn't choose extra_shot"

print("order:", coffee)