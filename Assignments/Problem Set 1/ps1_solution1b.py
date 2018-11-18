# Author: Razikh Shaik
# Problem Set 1

from ps1helper import request_user_input
from ps1helper import calculate_months_save


# Part b
# Write a program to calculate how many months it will take 
# you save up enough money for a downpayment.  LIke before, 
# assume that your investments earn a return of ​
# r​ = 0.04 (or 4%) and therequired down payment percentage 
# is 0.25 (or 25%).  Have the user enter the following 
# variables:
# 1.The starting annual salary (annual_salary)
# 2.The percentage of salary to be saved (portion_saved)
# 3.The cost of your dream home (total_cost)
# 4.The semi­annual salary raise (semi_annual_raise)

# Assumed Constants
portion_down_payment = 0.25
current_savings = 0
monthly_salary = 0
return_invst_rate_yearly = 0.04

# Output required
months_to_save = 0



annual_salary = request_user_input("The starting annual salary (as decimal):", type_expected =float)
portion_saved = request_user_input("The portion of salary to be saved (as fraction decimal):", float, range_expected={'low':0.0, 'high':100.00})
total_cost = request_user_input("The cost of your dream home (as decimal):", float)
semi_annual_raise = request_user_input("The semi­annual salary raise (as fraction decimal):", float, range_expected={'low':0.0})

monthly_salary = annual_salary/12
target_save_money = portion_down_payment * total_cost

months_to_save = calculate_months_save(current_savings, target_save_money,return_invst_rate_yearly, portion_saved, monthly_salary, semi_annual_raise=semi_annual_raise)

# Printing the output
print("Months to save:", months_to_save)