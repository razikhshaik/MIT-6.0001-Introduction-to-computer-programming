# Author: Razikh Shaik
# Problem Set 1

from ps1helper import request_user_input
from ps1helper import calculate_months_save


# Part c
# Write a program to calculate best interest using 
# bisection search.
# Have the user enter the following variables:
# 1.The starting annual salary (annual_salary)


# Assumed Constants
portion_down_payment = 0.25
current_savings = 0.0
monthly_salary = 0.0
return_invst_rate_yearly = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
months_to_save = 36
target_save_money = total_cost * portion_down_payment

# Output required
portion_saved = 0.0

annual_salary = request_user_input("The starting annual salary (as decimal):", type_expected =float)
monthly_salary = annual_salary/12

computed_months_to_save = 0
high = 1.0
low = 0.0
current = 0.5
steps = 0
portion_saved = current

fail_state = False

while months_to_save != computed_months_to_save:
    steps += 1
    computed_months_to_save = calculate_months_save(current_savings, 
        target_save_money,return_invst_rate_yearly, portion_saved, monthly_salary, 
        semi_annual_raise, acceptable_error= 100.00
    )
    if portion_saved == 1.0 and computed_months_to_save > 36:
        fail_state = True
        break
    if computed_months_to_save > months_to_save:
        portion_saved = (high + current)/2
        low = current
    else:
        portion_saved = (current + low)/2
        high = current
    current = portion_saved

    

# output
if not fail_state:
    print("Best Saving Rate:", round(portion_saved, 4))
    print("Steps taken:",steps)
else:
    print("It is not possible to pay the down payment in three years.")





