#rent calculator in python 

## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is(per person)
rent = int(input("Enter your hostle/flat rent ="))
food = int(input("Enter the amount of foodordered ="))
electricity_spend = int(input("Enter the total unit of electricity spend ="))
charge_per_unit = int(input("Enter the charge per unit ="))
person = int(input("Enter the number of persons living in hostle/flat ="))

total_electricity_bill = electricity_spend*charge_per_unit

output = (rent+food+total_electricity_bill) / person

print("Each person will pay =",output)
