import unittest
from unittest.mock import patch
import BabySitter
#Normally I would delete these skipped tests, but for the sake of showing my work I will just skip them
class TestTimeInput(unittest.TestCase):
    @unittest.skip("tests outdated code")
    def test_time_input_basic(self):
        self.assertEqual(BabySitter.timeInput(), 0)
    
    @unittest.skip("tests outdated code")
    @patch('BabySitter.timeInput', return_value='5pm')
    def test_time_input__one_input(self, input):
        result = BabySitter.timeInput()
        self.assertEqual(result, "5pm")
    
    @patch('BabySitter.timeInput', return_value= ['5pm', "3am", "10pm"])
    def test_time_input__three_inputs(self, input):
        result = BabySitter.timeInput()
        self.assertEqual(result, ['5pm', "3am", "10pm"])

    @patch('BabySitter.timeInput', return_value= ['7pm', "2am", "11pm"])
    def test_time_input__three_inputs2(self, input):
        result = BabySitter.timeInput()
        self.assertEqual(result, ['7pm', "2am", "11pm"])


class TestTimeValid(unittest.TestCase):
    @unittest.skip("tests outdated code") 
    def test_time_valid_basic(self):
        self.assertEqual(BabySitter.timeValid(), True)

    @unittest.skip("tests outdated code") 
    @patch('BabySitter.timeInput', return_value= ['7pm', "2am", "11pm"])
    def test_time_valid_1st_var_passed(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), "7pm")

    @unittest.skip("tests outdated code") 
    @patch('BabySitter.timeInput', return_value= ['7pm', "2am", "11pm"])
    def test_time_valid_2nd_var_passed(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), "2am")
    
    @unittest.skip("tests outdated code") 
    @patch('BabySitter.timeInput', return_value= ['7pm', "2am", "11pm"])
    def test_time_valid_3rd_var_passed(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), "11pm")

    @patch('BabySitter.timeInput', return_value= ['7Pas', "1234v", "11sadfpm"])
    def test_time_valid_time_wrong_formatting(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['7apm', "2am", "11pm"])
    def test_time_valid_time_almost_correct_formatting(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['7Pm', "2av", "11pm"])
    def test_time_valid_suffix_wrong_formatting(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])
    
    @patch('BabySitter.timeInput', return_value= ['7Pm', "2am", "11pM"])
    def test_time_valid_suffix_correct_formatting(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [7, 2, 11])

    @patch('BabySitter.timeInput', return_value= ['7pm', "2am", "11pm"])
    def test_time_valid_suffix_correct_formatting_without_lower(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [7, 2, 11])

    @patch('BabySitter.timeInput', return_value= ['2pm', "2am", "11pm"])
    def test_time_valid_too_early_start(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])
 
    @patch('BabySitter.timeInput', return_value= ['2am', "2am", "11pm"])
    def test_time_valid_too_late_start(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['4pm', "2am", "11pm"])
    def test_time_valid_too_early_start_border(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])
 
    @patch('BabySitter.timeInput', return_value= ['12am', "2am", "11pm"])
    def test_time_valid_too_late_start_border(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['11pm', "2am", "11pm"])
    def test_time_valid_correct_start_time(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [11, 2, 11])
    
    @patch('BabySitter.timeInput', return_value= ['5pm', "2am", "11pm"])
    def test_time_valid_correct_start_time_border(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [5, 2, 11])

    @patch('BabySitter.timeInput', return_value= ['6pm', "5pm", "11pm"])
    def test_time_valid_too_early_end(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['6pm', "8am", "11pm"])
    def test_time_valid_too_late_end(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['6pm', "5am", "11pm"])
    def test_time_valid_too_late_end_border(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['6pm', "2am", "11pm"])
    def test_time_valid_correct_end(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [6, 2, 11])

    @patch('BabySitter.timeInput', return_value= ['6pm', "4am", "11pm"])
    def test_time_valid_correct_end_border(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [6, 4, 11])
    
    @patch('BabySitter.timeInput', return_value= ['6pm', "12am", "11pm"])
    def test_time_valid_correct_end_midnight(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [6, 12, 11])

    @patch('BabySitter.timeInput', return_value= ['12am', "12am", "11pm"])
    def test_time_valid_incorrect_end_start_same(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['8pm', "1am", "9pm"])
    def test_time_valid_correct_bed_start_1_digit(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [8, 1, 9])

    @patch('BabySitter.timeInput', return_value= ['8pm', "1am", "9pm"])
    def test_time_valid_correct_bed_1_digit_pm(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [8, 1, 9])

    @patch('BabySitter.timeInput', return_value= ['8pm', "1am", "6pm"])
    def test_time_valid_incorrect_bed_start_1_digit_pm(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['8pm', "2am", "1am"])
    def test_time_valid_incorrect_bed_1_digit_am(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])

    @patch('BabySitter.timeInput', return_value= ['8pm', "1am", "11pm"])
    def test_time_valid_correct_bed_2_digit_pm(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [8, 1, 11])

    @patch('BabySitter.timeInput', return_value= ['8pm', "10pm", "11pm"])
    def test_time_valid_incorrect_bed_start_2_digit_pm(self,input):
        self.assertEqual(BabySitter.timeValid(BabySitter.timeInput()), [])


class TestCalculatePay(unittest.TestCase):

    @unittest.skip("tests outdated code") 
    @patch('BabySitter.timeInput', return_value= [8, 2, 11])
    def test_calculate_pay_basic(self,input):
        self.assertEqual(BabySitter.calulatePay(BabySitter.timeInput()), 0)

    @patch('BabySitter.timeInput', return_value= [8, 2, 11])
    def test_calculate_pay(self,input):
        self.assertEqual(BabySitter.calulatePay(BabySitter.timeInput()), 76)
    
    @patch('BabySitter.timeInput', return_value= [5, 4, 9])
    def test_calculate_pay_big_amount(self,input):
        self.assertEqual(BabySitter.calulatePay(BabySitter.timeInput()), 136)

    @patch('BabySitter.timeInput', return_value= [9, 4, 9])
    def test_calculate_pay_same_start_bed(self,input):
        self.assertEqual(BabySitter.calulatePay(BabySitter.timeInput()), 88)

    @patch('BabySitter.timeInput', return_value= [9, 11, 11])
    def test_calculate_pay_same_bed_end(self,input):
        self.assertEqual(BabySitter.calulatePay(BabySitter.timeInput()), 24)

    @patch('BabySitter.timeInput', return_value= [7, 3, 10])
    def test_calculate_pay2(self,input):
        self.assertEqual(BabySitter.calulatePay(BabySitter.timeInput()), 100)




#I performed manual integration tests with values I tried here and with the Debugger to confirm