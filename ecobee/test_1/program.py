#!/usr/bin/python
import pdb
import json

'''
Test 1:
Write a working program code that will take the test_results.json file as an 
input and provide:
1) For each test suite:
x Test suite name
x Print out the total number of tests that passed and their details
x Print out the total number of tests that failed and their details
x Print out the total number of test that are blocked
x Print out the total number of test that took more than 10 seconds to execute
2) Proper treatment for common error conditions
3) All the detail lists need to be printed in ascending order
4) Speed is first priority, memory is secondary
5) Java or Python
'''

def get_number_of_tests(test_results,result):
    '''
    Gets total number of tests that has certain result and its details

    Parameters
    ----------
    test_results: list
        The results of the tests
    result: string 
        the resul we are looking for in the tests

    Returns
    -------
    total_number_of_tests: int 
        Total number of tests that has certain result
        0 if none if found
    test_details: list
        details of the tests that meet the results
        [] empty list if none is found
    '''
    total_number_of_tests = 0
    test_details = []
    for test_result in test_results:
        if test_result.get('status') == result:
            total_number_of_tests += 1
            test_details.append(test_result)
    return total_number_of_tests, test_details

def print_test_details(test_details):
    '''
    It prints the test details for a nice view in the screen
    '''
    for test_detail in test_details:
        # Test details are:
        status = test_detail.get('status')
        time = test_detail.get('time')
        name = test_detail.get('test_name')
        message = '\t\tStatus: {0}\t'.format(status)
        message += 'Time: {0}\tName: {1}'.format(status, time, name)
        print(message)

# Read the file with the results
test_result_dictionary = {}
with open('file.json') as file:
    test_result_dictionary = json.load(file)

# Print the information of the results
for test_suite in test_result_dictionary.get('test_suites'):
    # Test suite name
    print('Test suite name: ' + test_suite['suite_name'])
    # Print out the total number of tests that passed and their details
    results = test_suite.get('results')
    passed_tests, test_details = get_number_of_tests(results, 'pass')
    print('\tPassed tests: ' + str(passed_tests))
    print_test_details(test_details)






