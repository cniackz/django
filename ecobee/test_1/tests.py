import unittest
from print_report import get_number_of_tests
from print_report import print_test_details
from print_report import print_results
from print_report import display_report
from print_report import helper_funtion

class TestStringMethods(unittest.TestCase):

    errors = {
        'no_error': 0,
        'invalid_test_suites': 1,
        'invalid_suite_name': 2,
        'invalid_results': 3,
    }

    def test_helper_function(self):
        test_input = [
            {'test_name': 'test_eco_2624', 'time': '', 'status': 'blocked'},
            {'test_name': 'test_eco_2641', 'time': '', 'status': 'blocked'}
        ]
        actual_result = helper_funtion(test_input)
        expected_result = [
            {'test_name': 'test_eco_2624', 'time': '', 'status': 'blocked'},
            {'test_name': 'test_eco_2641', 'time': '', 'status': 'blocked'}
        ]
        self.assertEqual(actual_result, expected_result)

    def test_get_number_of_tests_on_corrupted_file(self):
        test_results = [ 1,2,3,
            {'status': 'pass', 'time': '8.556', 'test_name': 'test_eco_2621'},
            {'status': 'pass', 'time': '45.909', 'test_name': 'test_eco_1725'},
            {'status': 'fail', 'test_name': ' test_eco_2645'},
            {'stus': 'pass', 'time': '6.719', 'tesame': 'test_eco_2623'},
            {'status': 'blocked', 'time': '', 'test_name': 'test_eco_2624'},
            {'status': 'pass', 'time': '8.017', 'testme': 'test_eco_2625'},
            {'status': 'pass', 'time': '8.774', 'test_name': 'test_eco_2626'},
            {'status': 'blocked', 'time': '', 'test_name': 'test_eco_2641'},
            {'stus': 'pass', 'time': '4.967', 'test_name': 'test_eco_2622'},
            {'status': 'fail', 'time': '12.690', 'tename': 'test_eco_2782'},
            {'status': 'fail', 'time': '70.902', 'test_name': 'test_eco_2633'}
        ]
        result_names = ('pass', 'fail', 'blocked')
        actual_result = get_number_of_tests(test_results, result_names)
        expected_result = self.errors['invalid_results']
        self.assertEqual(actual_result, expected_result)

    def test_get_number_of_tests(self):
        test_results = [
            {'status': 'pass', 'time': '8.556', 'test_name': 'test_eco_2621'},
            {'status': 'pass', 'time': '45.909', 'test_name': 'test_eco_1725'},
            {'status': 'fail', 'time': '9.383', 'test_name': ' test_eco_2645'},
            {'status': 'pass', 'time': '6.719', 'test_name': 'test_eco_2623'},
            {'status': 'blocked', 'time': '', 'test_name': 'test_eco_2624'},
            {'status': 'pass', 'time': '8.017', 'test_name': 'test_eco_2625'},
            {'status': 'pass', 'time': '8.774', 'test_name': 'test_eco_2626'},
            {'status': 'blocked', 'time': '', 'test_name': 'test_eco_2641'},
            {'status': 'pass', 'time': '4.967', 'test_name': 'test_eco_2622'},
            {'status': 'fail', 'time': '12.690', 'test_name': 'test_eco_2782'},
            {'status': 'fail', 'time': '70.902', 'test_name': 'test_eco_2633'}
        ]
        result_names = ('pass', 'fail', 'blocked')
        actual_result = get_number_of_tests(test_results, result_names)
        expected_result = {
            'fail': [
                {u'status': u'fail', u'time': u'9.383', u'test_name': u' test_eco_2645'},
                {u'status': u'fail', u'time': u'12.690', u'test_name': u'test_eco_2782'},
                {u'status': u'fail', u'time': u'70.902', u'test_name': u'test_eco_2633'}
            ],
            'blocked': [
                {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2624'},
                {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2641'}
            ],
            'pass': [
                {u'status': u'pass', u'time': u'8.556', u'test_name': u'test_eco_2621'},
                {u'status': u'pass', u'time': u'45.909', u'test_name': u'test_eco_1725'},
                {u'status': u'pass', u'time': u'6.719', u'test_name': u'test_eco_2623'},
                {u'status': u'pass', u'time': u'8.017', u'test_name': u'test_eco_2625'},
                {u'status': u'pass', u'time': u'8.774', u'test_name': u'test_eco_2626'},
                {u'status': u'pass', u'time': u'4.967', u'test_name': u'test_eco_2622'}],
            'slow_tests': 3
        }
        self.assertEqual(actual_result, expected_result)

    def test_print_test_details(self):
        test_details = [
            {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2624'},
            {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2641'}
        ]
        result = print_test_details(test_details)
        expected_result = [
            '\t\tName: test_eco_2624\tTime: ',
            '\t\tName: test_eco_2641\tTime: '
        ]
        actual_result = result
        self.assertEqual(actual_result, expected_result)

    def test_print_results(self):
        results = [
            {u'status': u'pass', u'time': u'8.556', u'test_name': u'test_eco_2621'},
            {u'status': u'pass', u'time': u'45.909', u'test_name': u'test_eco_1725'},
            {u'status': u'fail', u'time': u'9.383', u'test_name': u' test_eco_2645'},
            {u'status': u'pass', u'time': u'6.719', u'test_name': u'test_eco_2623'},
            {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2624'},
            {u'status': u'pass', u'time': u'8.017', u'test_name': u'test_eco_2625'},
            {u'status': u'pass', u'time': u'8.774', u'test_name': u'test_eco_2626'},
            {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2641'},
            {u'status': u'pass', u'time': u'4.967', u'test_name': u'test_eco_2622'},
            {u'status': u'fail', u'time': u'12.690', u'test_name': u'test_eco_2782'},
            {u'status': u'fail', u'time': u'70.902', u'test_name': u'test_eco_2633'}
        ]
        actual_result = print_results(results)
        expected_result = [
            '\tblocked: 2',
            '\tfail: 3',
            '\tpass: 6',
            '\tSlow tests: 3 (took more than 10 seconds)'
        ]
        self.assertEqual(actual_result, expected_result)

    def test_display_report(self):
        test_result_dictionary = {
            u'test_suites': [
                {
                    u'suite_name': u'hvac_mode',
                    u'results': [
                        {u'status': u'pass', u'time': u'8.556', u'test_name': u'test_eco_2621'},
                        {u'status': u'pass', u'time': u'45.909', u'test_name': u'test_eco_1725'},
                        {u'status': u'fail', u'time': u'9.383', u'test_name': u' test_eco_2645'},
                        {u'status': u'pass', u'time': u'6.719', u'test_name': u'test_eco_2623'},
                        {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2624'},
                        {u'status': u'pass', u'time': u'8.017', u'test_name': u'test_eco_2625'},
                        {u'status': u'pass', u'time': u'8.774', u'test_name': u'test_eco_2626'},
                        {u'status': u'blocked', u'time': u'', u'test_name': u'test_eco_2641'},
                        {u'status': u'pass', u'time': u'4.967', u'test_name': u'test_eco_2622'},
                        {u'status': u'fail', u'time': u'12.690', u'test_name': u'test_eco_2782'},
                        {u'status': u'fail', u'time': u'70.902', u'test_name': u'test_eco_2633'}
                    ]
                },
                {
                    u'suite_name': u'temp_setting',
                    u'results': [
                        {u'status': u'fail', u'time': u'5.890', u'test_name': u'test_eco_2915'},
                        {u'status': u'fail', u'time': u'10.000', u'test_name': u'test_eco_2913'}
                    ]
                }
            ]
        }
        actual_result = display_report(test_result_dictionary)
        expected_result = [
            'Test suite name: hvac_mode\n',
            'Test suite name: temp_setting\n'
        ]
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()