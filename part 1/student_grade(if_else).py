# Input
name = input("Input Student Name: ")
score = int(input("Input Student Score: "))
grade = None

#Grade Condition
if score < 0 or score > 100:
    print("invalid input")
elif 85 <= score:
    grade = "A"
elif 75 <= score < 85:
    grade = "B"
elif 55 <= score < 75:
    grade = "C"
elif 40 <= score < 55:
    grade = "D"
elif 0 <= score < 40:
    grade = "E"


#Output
if grade is not None:
    print("========== Summary ==========")
    print(f"Name: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    if grade in ("A", "B", "C"):
        print(f"Status: Passed")
    else:
        print(f"Status: Failed")

