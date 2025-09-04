# TI-84 Plus CE Python Edition: Show the Ten Rules for Divisibility

def show_divisibility_rules():
    rules = [
        "1. Divisible by 2: The last digit is even (0, 2, 4, 6, 8).",
        "2. Divisible by 3: The sum of the digits is divisible by 3.",
        "3. Divisible by 4: The last two digits form a number divisible by 4.",
        "4. Divisible by 5: The last digit is 0 or 5.",
        "5. Divisible by 6: The number is divisible by both 2 and 3.",
        "6. Divisible by 7: Double the last digit, subtract from the rest; result is divisible by 7.",
        "7. Divisible by 8: The last three digits form a number divisible by 8.",
        "8. Divisible by 9: The sum of the digits is divisible by 9.",
        "9. Divisible by 10: The last digit is 0.",
        "10. Divisible by 11: The difference between the sum of the odd and even placed digits is divisible by 11."
    ]
    print("The Ten Rules for Divisibility:")
    for rule in rules:
        print(rule)

# Simulate running the ":D:" code
def run_code(code):
    if code == ":D:":
        show_divisibility_rules()
    else:
        print("Unknown code.")

# Example usage:
if __name__ == "__main__":
    user_code = input("Enter code to run: ")
    run_code(user_code)