# Description: Program to enter and calculate new insurance policy information for customers
# Date: March 14, 2024 -  March 18, 2024
# Author: Shane Young

# Import libraries.
import FormatValues as FV
import datetime

# Define program constants.
NEXT_POLICY_NUM = 1944
BASIC_PREM_RATE = 869.00
ADD_CAR_DISC_RATE = 0.25
EXTRA_LIABILITY_RATE = 130.00
GLASS_COVERAGE_RATE = 86.00
LOANER_CAR_RATE = 58.00
HST_RATE = 0.15
MONTH_PROCESS_RATE = 39.99

f = open('def.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
f.close()

# Defining dates
CURRENT_DATE = datetime.datetime.now()
invoice_date = CURRENT_DATE.date()
try:
	payment_date = datetime.date(invoice_date.year, invoice_date.month + 1, 1)
except:
	payment_date = datetime.date(invoice_date.year + 1, 1, 1)
else:
	pass

# Validation Lists
prov_list = ['NL', 'NB', 'NS', 'PE', 'QC', 'ON', 'SK', 'MB', 'AB', 'BC', 'YT', 'NT', 'NU']
payment_options_list = ['Full', 'Monthly', 'Down Pay']


# Define program functions (need 3 for program)
def calculate_insurance_premium(num_cars):
	inital_car_amt = BASIC_PREM_RATE
	add_car_amt = (num_cars - 1) * (BASIC_PREM_RATE - (BASIC_PREM_RATE * ADD_CAR_DISC_RATE))
	insurace_prem = inital_car_amt + add_car_amt


	return insurace_prem

def format_yes_no(input):
	if input == "Y":
		input_display = "Yes"
	elif input == "N":
		input_display = "No"
	else:
		input_display == ""
	
	return input_display

def calculate_extras(num_cars, extra_liability, optional_glass, optional_loaner):
	if extra_liability == "Y":
		extra_liab_amt = EXTRA_LIABILITY_RATE * num_cars
	else:
		extra_liab_amt = 0
	
	if optional_glass == "Y":
		option_glass_amt = GLASS_COVERAGE_RATE * num_cars
	else:
		option_glass_amt = 0
	
	if optional_loaner == "Y":
		optional_loaner_amt = LOANER_CAR_RATE * num_cars
	else:
		optional_loaner_amt = 0
	
	total_extras = extra_liab_amt + option_glass_amt + optional_loaner_amt
	return extra_liab_amt, option_glass_amt, optional_loaner_amt, total_extras

# Main program.
while True:
	# Gather user inputs
	print()
	first_name = input("Enter customer's first name (END to stop the program): ").title()
	if first_name == "End":
		break
	last_name = input("Enter customer's last name: ").title()
	address = input("Enter customer's street address: ")
	city = input("Enter customer's city: ").title()
	while True:
		province = input("Enter customers province (AA): ").upper()
		if province not in prov_list:
			print("Error - Incorrect province code, please re-enter.")
			print()
		else:
			break
	postal_code = input("Enter customer's postal code (A1A1A1): ").upper()
	phone_number = input("Enter the customer's phone number (##########): ")
	print()

	while True:
		num_cars = int(input("Enter the number of cars being insured: "))
		if num_cars < 1:
			print("Error - Number of cars must be greater than 0, please re-enter.")
		else:
			break
	extra_liability = input("Would the customer like extra liability coverage up to $1,000,000? (Y/N) ").upper()
	optional_glass = input("Would the customer like to purchase optional glass coverage? (Y/N): ").upper()
	optional_loaner = input("Would the customer like to purchase a loaner vehicle? (Y/N): ").upper()

	while True:
		payment_options = input("How would the customer like to pay? (Full, Monthly or Down Pay): ").title()
		if payment_options not in payment_options_list:
			print("Error - Not a valid payment option, please enter Full, Monthly or Down Pay")
		else:
			break
	if payment_options == 'Down Pay':
		down_payment = float(input("Please enter the amount of the down payment: $ "))
	else:
		down_payment = 0
	print()
	print("Please enter all of the customers previous claims below")
	print()
	
	claim_num_list = []
	claim_date_list = []
	claim_amt_list = []
	while True:
		claim_num = input("Enter the claim number: ")
		claim_num_list.append(claim_num)
		claim_date = input("Enter the claim date (YYYY-MM-DD): ")
		claim_date_list.append(claim_date)
		claim_amt = float(input("Enter the claim amount (#####.##): $ "))
		claim_amt_list.append(claim_amt)
		print()
		claim_continue = input('Would you like to process another claim? (Y/N): ').upper()
		if claim_continue == "N":
			break

	# Perform required calculations.
		
	# Calcluating insurance premiums and additional costs
	insurance_prem = calculate_insurance_premium(num_cars)

	# Calculating extra options cost
	extra_liab_amt, option_glass_amt, optional_loaner_amt, total_extras = calculate_extras(num_cars, extra_liability, optional_glass, optional_loaner)

	# Calculating totals
	total_insurance_prem = insurance_prem + total_extras
	hst_amt = total_insurance_prem * HST_RATE
	total_cost = total_insurance_prem + hst_amt

	# Calculating Monthly Payment Options
	monthly_paymemt = (total_cost + MONTH_PROCESS_RATE) / 8
	if payment_options == 'Down Pay':
		monthly_paymemt = ((total_cost + MONTH_PROCESS_RATE) - down_payment) / 8

	# Display results.

	print()
	print(f'One Stop Insurance Company                    Invoice Date: {FV.FDateM(invoice_date)}')
	print(f'Insurance Policy Receipt                      Policy Number: {NEXT_POLICY_NUM}')
	print(f'--------------------------')
	print(f'--------------------------                    Base Insurance Premium:   {FV.FDollar2(insurance_prem):>9s}')
	print(f'                                              Extra Liability Amount:   {FV.FDollar2(extra_liab_amt):>9s}')
	print(f'Customer Information:                         Optional Glass Amount:    {FV.FDollar2(option_glass_amt):>9s}')
	print(f'                                              Optional Loaner Amount:   {FV.FDollar2(optional_loaner_amt):>9s}')
	print(f'	{first_name} {last_name}')
	print(f'	{address:<25s}             Total Extras:             {FV.FDollar2(total_extras):>9s}')
	print(f'	{city:<14s}, {province:<2s} {postal_code:<6s}             Total Premium:            {FV.FDollar2(total_insurance_prem):>9s}')
	print(f'	Phone Number: {phone_number:>11s}             HST:                      {FV.FDollar2(hst_amt):>9s}')
	print(f'                                                                        ---------')
	print(f'Policy Details:                               Total Cost:               {FV.FDollar2(total_cost):>9s}')
	print(f'                                              -----------------------------------')
	print(f'	# of Cars to Insure:  {num_cars:<2d}')
	print(f'	Extra Liability:      {format_yes_no(extra_liability):<3s}             Monthly Payment Option')
	print(f'	Optional Glass:       {format_yes_no(optional_glass):<3s}             -----------------------------------')
	print(f'	Optional Loaner:      {format_yes_no(optional_loaner):<3s}             Monthly Payment:    {FV.FDollar2(monthly_paymemt)}')
	print(f'	Payment Method:       {payment_options:<8s}        First Payment Date: {FV.FDateM(payment_date)}')
	if payment_options == "Down Pay":
		print(f'	Down Payment:         {FV.FDollar2(down_payment):<9s}')

	print()
	print(f'---------------------------------------------------------------------------------')
	print(f'                               Previous Claim History                            ')
	print(f'                             --------------------------                          ')
	print()
	print(f'                    Claim Number        Claim Date          Amount               ')
	print(f'                 ----------------------------------------------------            ')
	for num in range(len(claim_num_list)):
		claim_num = claim_num_list[num]
		claim_date = claim_date_list[num]
		claim_amt = claim_amt_list[num]
		print(f'                       {claim_num:<5s}            {claim_date:<9s}          {FV.FDollar2(claim_amt):>9s}            ')	
	
	f = open("policies.dat", "a")
	f.write("{}, ".format(str(NEXT_POLICY_NUM)))
	f.write("{}, ".format(first_name))
	f.write("{}, ".format(last_name))
	f.write("{}, ".format(address))
	f.write("{}, ".format(city))
	f.write("{}, ".format(province))
	f.write("{}, ".format(postal_code))
	f.write("{}, ".format(phone_number))
	f.write("{}, ".format(str(num_cars)))
	f.write("{}, ".format(extra_liability))
	f.write("{}, ".format(optional_glass))
	f.write("{}, ".format(optional_loaner))
	f.write("{}, ".format(payment_options))
	f.write("{}, ".format(str(down_payment)))
	f.write("{}, ".format(claim_num_list))
	f.write("{}, ".format(claim_date_list))
	f.write("{}, ".format(claim_amt_list))
	f.write("{}\n".format(str(total_insurance_prem)))
	f.close()

	NEXT_POLICY_NUM += 1

	f = open('def.dat', 'w')
	f.write('{}\n'.format(str(NEXT_POLICY_NUM)))
	f.close()

	print()
	print("This policy data and customer's previous claim data has been saved!")
# Housekeeping.
print()
print("Thank you for using the program!")