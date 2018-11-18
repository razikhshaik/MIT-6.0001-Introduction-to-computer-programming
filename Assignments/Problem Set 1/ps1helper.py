# All imports
import traceback        # To print detailed error messages

def request_user_input(request_string, type_expected, range_expected = None, non_negative= True):
    while True:
        try:
            requested_output = type_expected(input(request_string))
            if not (non_negative == True and (type_expected == int or type_expected == float) and requested_output >= 0):
                raise Exception("Please enter postive value")
            if range_expected != None:
                if type_expected == int or type_expected == float:
                    assert requested_output >= range_expected['low']
                    if 'high' in range_expected:
                        assert requested_output <= range_expected['high']
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

def calculate_months_save(current_savings, target_save_money,return_invst_rate_yearly, portion_saved, monthly_salary, semi_annual_raise = 0, acceptable_error = 0):
    months_to_save = 0
    while (current_savings - target_save_money < acceptable_error) or (current_savings - target_save_money < -1*acceptable_error):
        current_savings += (current_savings*return_invst_rate_yearly/12)
        current_savings += portion_saved * monthly_salary
        months_to_save += 1
        if months_to_save % 6 == 0:
            monthly_salary += (monthly_salary*semi_annual_raise)
    return months_to_save