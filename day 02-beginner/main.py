print("=========================================")
print("==== Welcome to the tips calculator? ====")
print("=========================================")


bill = float(input("What is the total bill amount? \n--> $: "))
tip = float(input("How many tip would you like to give? \n--> Percent (%): "))
people = int(input("How many people to split the bill? \n--> People: "))

total = (bill * (tip/100) + bill) / people

print(f"Each people should pay: {total:.2f} $")