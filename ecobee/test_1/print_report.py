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
    x Print out the total number of test that are blocked and their details
    x Print out the total number of test that took more than 10 seconds
2) Proper treatment for common error conditions
3) All the detail lists need to be printed in ascending order
4) Speed is first priority, memory is secondary
5) Java or Python
'''

errors = {
    'no_error': 0,
    'invalid_test_suites': 1,
    'invalid_suite_name': 2,
    'invalid_results': 3,
}

# Functions
def get_number_of_tests(test_results,result_names):
    '''
    Gets total number of tests per result_name and its details

    Parameters
    ----------
    test_results: list
        The results of the tests
    result_names: list
        the results we are looking for in the tests
        - result_name: pass
        - result_name: fail
        - result_name: blocked

    Returns
    -------
    test_details: dict
        details of the tests per result_name plus number of tests that took more
        than 10 seconds to be executed.
    '''
    def check_per_result_name(test_details, test_result):
        '''
        Check the result per row to group it under a result_name
        '''
        result = None
        for result_name in result_names:
            # Proper treatment for common error conditions
            if isinstance(test_result, int):
                result = errors['invalid_results']
            else:
                if test_result.get('status') == result_name:
                    if test_details.get(result_name):
                        test_details[result_name].append(test_result)
                    else:
                        test_details[result_name] = [test_result]
        return result

    test_details = {}
    test_details['slow_tests'] = 0
    for test_result in test_results:
        if isinstance(test_result, int):
            test_details = errors['invalid_results']
            break
        result = check_per_result_name(test_details, test_result)
        if result:
            # File is broken
            test_details = result
            break
        else:
            if test_result.get('time'):
                if float(test_result['time']) > 10:
                    test_details['slow_tests'] += 1

    return test_details

def helper_funtion(list_of_dicts):
    '''
    To sort a list of dictionaries by a time key
    '''

    # Get all the times
    list_of_times = []
    for dictionary in list_of_dicts:
        try:
            list_of_times.append(float(dictionary['time']))
        except:
            list_of_times.append(0)

    # Sort the times
    list_of_times.sort()

    # Sort the dictonaries
    local_list_of_dictionaries = []
    for index, time in enumerate(list_of_times):
        for dictionary in list_of_dicts:
            if time == 0:
                time = ''
            else:
                time = str(time)
            if dictionary['time'] == time:
                local_list_of_dictionaries.insert(index,dictionary)
                list_of_dicts.remove(dictionary)
                break

    return local_list_of_dictionaries

def print_test_details(test_details):
    '''
    It prints the test details for a nice view in the screen
    '''
    # All the detail lists need to be printed in ascending order
    # Sort a list of dictionaries by a value of the dictionary
    result = []
    import operator
    #import pdb; pdb.set_trace();
    #test_details = sorted(test_details, key=lambda k: k['test_name'].strip())
    #test_details = sorted(test_details, key=lambda k: k['time'].strip())
    #import pdb; pdb.set_trace();
    #test_details = test_details.sort(key=operator.itemgetter('time'))
    #test_details = sorted(test_details, key=lambda k: k['time'])
    test_details = helper_funtion(test_details)

    #import pdb; pdb.set_trace();
    #for item in test_details:
    #for dictionary in test_details

    for test_detail in test_details:
        # Test details are:
        status = test_detail.get('status')
        time = test_detail.get('time')
        name = test_detail.get('test_name').strip()
        message = '\t\tName: {0}\t'.format(name)
        message += 'Time: {0}'.format(time)
        print(message)
        result.append(message)
    return result

def print_results(results):
    '''
    It prints the results of the different categories:
    1. Pass
    2. Fail
    3. Blocked
    '''
    final_result = []
    result_names = ('pass', 'fail', 'blocked')
    test_details = get_number_of_tests(results, result_names)
    if test_details in [errors[error] for error in errors]:
        # File is broken, dont proceed
        final_result = test_details
    else:
        # All the detail lists need to be printed in ascending order
        # blocked, fail, pass, slow
        for result in sorted(test_details):
            if isinstance(test_details[result], int):
                # Print out the total number of test that took more than 10 secs
                message = '\tSlow tests: {0}'.format(test_details[result])
                message += ' (took more than 10 seconds)'
                print(message)
                final_result.append(message)
            else:
                number_of_tests = len(test_details[result])
                message = '\t{0}: {1}'.format(result, number_of_tests)
                print(message)
                final_result.append(message)
                print_test_details(test_details[result])
    return final_result

def display_report(test_result_dictionary):
    '''
    Print the information of the results
    '''
    final_result = []
    # Sort a list of dictionaries by a value of the dictionary
    suites = test_result_dictionary.get('test_suites')
    suites = sorted(suites, key=lambda k: k['suite_name'].strip())
    for test_suite in suites:

        # Test suite name
        print('')
        message = 'Test suite name: {0}\n'.format(test_suite['suite_name'])
        print(message)
        final_result.append(message)
        results = test_suite.get('results')
        result = print_results(results)
        if result in [errors[error] for error in errors]:
            # broken file
            final_result = result
            break

    print('')
    return final_result # Mainly for testing

def main(file):
    test_result_dictionary = {}
    try:
        file = open(file,'r')
        test_result_dictionary = json.load(file)
        file.close()
    except Exception as e:
        print('We could not read the json file due to {0!r}'.format(e))

    if test_result_dictionary:
        result = display_report(test_result_dictionary)
        if result:
            for error in errors:
                if errors[error] == result:
                    print(error)

# Running the script directly from command line
if __name__ == '__main__':
    '''
    Read the file
    If file content is available then call the script
    '''
    main('file.json')

