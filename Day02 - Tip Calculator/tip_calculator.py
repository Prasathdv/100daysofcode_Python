# This is a tips calculator. This also split up cost accrued between friends equally including tips %.

# Print Welcome message for Tip Calculator
print("Welcome to the tip calculator.")

# Get Total bill
total_bill = float(input("What was the total bill? $"))

# Get number of persons to split the amount
split_number = int(input("How many people to split the bill? "))

# What percentage tips to give 10,12 or 15
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

# Tip calculation
split_amount = round(
    ((total_bill + (tip_percentage/100 * total_bill))/split_number), 1)

print(f"Each person should pay: ${split_amount}")
