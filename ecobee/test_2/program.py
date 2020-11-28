import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Test 2
Write a working program using Selenium Webdriver that will do:
• Browse to http://slashdot.org/
• Print how many articles are on the page
• Print a list of unique (different) icons used on article titles and how many times was it used
• Vote for some random option on the daily poll
• Return the number of people that have voted for that same option
• Java or Python
'''

driver = webdriver.Chrome('/Users/ccelis/django/ecobee/test_2/chromedriver')