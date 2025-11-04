distance = int(input("Enter the distance:-"))

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "car"

print("AI suggest you can go through->", transport)