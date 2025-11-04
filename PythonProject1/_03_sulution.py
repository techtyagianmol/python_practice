marks = int(input("enter your marks in 100:-"))

if marks > 100:
    print("not a valid marks")
elif marks <=33:
    print("fail,","you got->Grade-f")
elif marks < 50:
    print("pass,","you got->grade-c")
elif marks < 70:
    print("you can do better,","you got->grade-b")
else:
    print("excellent,","you got->grade-a")