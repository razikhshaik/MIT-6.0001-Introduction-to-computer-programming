# Author: Razikh Shaik
# Problem Set 1

# All imports
import traceback        # To print detailed error messages



# Part a
# Write a program to calculate how many months it will take you to save up enough money for a down
# payment. You will want your main variables to be floats, so you should cast user inputs to floats.   
# Your program should ask the user to enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The portion of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)

# Assumed Constants
portion_down_payment = 0.25
current_savings = 0
monthly_salary = 0
return_invst_rate_yearly = 0.04

# Output required
months_to_save = 0

def request_user_input(request_string, type_expected, range_expected = None, non_negative= True):
    while True:
        try:
            requested_output = type_expected(input(request_string))
            if not (non_negative == True and (type_expected == int or type_expected == float) and requested_output >= 0):
                raise Exception("Please enter postive value")
            if range_expected != None:
                if type_expected == int or type_expected == float:
                    assert requested_output >= range_expected['low'] and requested_output <= range_expected['high']
                else:
                    raise Exception("input expected is non numeric but expected range is numeric")
            return requested_output
        except AssertionError as Ae:
            if range_expected != None:
                print(requested_output, "incorrect, expected range:[",range_expected['low'], range_expected['high'],"]")
        except ValueError as ve:
            print('Value Error')
        except:
            print(traceback.format_exc())  

annual_salary = request_user_input("The starting annual salary (as decimal):", type_expected =float)
portion_saved = request_user_input("The portion of salary to be saved (as fraction decimal):", float, range_expected={'low':0.0, 'high':100.00})
total_cost = request_user_input("The cost of your dream home (as decimal):", float)

monthly_salary = annual_salary/12
target_save_money = portion_down_payment * total_cost

while current_savings < target_save_money:
    current_savings += (current_savings*return_invst_rate_yearly/12)
    current_savings += portion_saved * monthly_salary
    months_to_save += 1

print(current_savings, target_save_money)
# Printing the output
print("Months to save:", months_to_save)