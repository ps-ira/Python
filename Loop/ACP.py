def is_as_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = 0

    for digit in num_str:
        digit_int = int(digit)
        sum_of_powers += digit_int ** num_digits
    
    if sum_of_powers == num:
        return True
    else:
        return False
    
number = int(input("Enter a number: "))
if is_as_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
