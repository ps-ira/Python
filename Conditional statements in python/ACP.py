def check_eligibility(age, score):
    if age < 12:
        return "You are not eligible because you must be 12 or older to take the exam."
    elif score < 70:
        return "You are not eligible because your score is below the required minimum of 70."
    else:
        return "Congratulations! You are eligible to take the exam."

age = int(input("Enter your age: "))
score = float(input("Enter your score: "))
result = check_eligibility(age, score)
print(result)
