if not (non_negative == True and (type_expected == int or type_expected == float) and requested_output >= 0):
                raise Exception("Please enter postive value")
            if type(range_expected) == dict:
                print("poop")
                if type_expected == int or type_expected == float:
                    assert requested_output >= range_expected['low'] and requested_output >= range_expected['low']
                else:
                    raise Exception("input expected is non numeric but expected range is numeric")