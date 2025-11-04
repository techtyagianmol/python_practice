weather = input("enter weather condition:-")

if weather == "sunny":
    activity = "activity->Go for walk or you can rest"
elif weather == "rainy":
    activity = "activity->Read a book"
elif weather == "snowy":
    activity = "activity->Build a snowman"

print(activity)