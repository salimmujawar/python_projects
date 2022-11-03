# Tip Calculator
print("Welcome to Tip Calculator");
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip you would like to give? 10,12, or 15? $"))
people = int(input("How many people to split the bill?"))

tip_percentage = tip / 100
tip_with_percentage = bill * tip_percentage
bill_with_tip = bill + tip_with_percentage

bill_per_person = bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
