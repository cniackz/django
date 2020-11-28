import pdb
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Test 2
Write a working program using Selenium Webdriver that will do:
* Browse to http://slashdot.org/
* Print how many articles are on the page
* Print a list of unique (different) icons used on article titles and how many
  times was it used
* Vote for some random option on the daily poll
* Return the number of people that have voted for that same option
'''

class TestStringMethods(unittest.TestCase):

    driver = None
    selectors = {
        'articles': """//*[@id="firehoselist"]/article[@data-fhid]""",
        'icons': """//*[@id="firehoselist"]/article[@data-fhid]/header/span/a/img"""
    }

    def setUp(self):
        path_to_binary = '/Users/ccelis/django/ecobee/test_2/chromedriver'
        self.driver = webdriver.Chrome(path_to_binary)

    def wait(self, driver, selector):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )

    def test_count_articles(self):
        '''
        Print how many articles are on the page
        '''
        driver = self.driver
        selectors = self.selectors
        # Browse to http://slashdot.org/
        driver.get('http://slashdot.org/')
        self.wait(driver, selectors['articles'])
        articles = driver.find_elements_by_xpath(selectors['articles'])
        number_of_articles = len(articles)
        # Print how many articles are on the page
        print('Number of articles on the page {0}'.format(number_of_articles))

    def test_get_unique_icons(self):
        '''
        Print a list of unique (different) icons used on article titles and
        how many times was it used
        '''
        driver = self.driver
        selectors = self.selectors
        # Visit the page
        driver.get('http://slashdot.org/')
        # Wait for articles to be present
        self.wait(driver, selectors['articles'])
        icons = driver.find_elements_by_xpath(selectors['icons'])
        unique_icons = {}
        for icon in icons:
            if unique_icons.get(icon.get_attribute('title')):
                unique_icons[icon.get_attribute('title')] += 1
            else:
                unique_icons[icon.get_attribute('title')] = 1
        for icon, used in unique_icons.items():
            print('icon: {0}, used: {1}'.format(icon,used))

    def test_vote_on_daily_poll(self):
        '''
        Vote for some random option on the daily poll
        '''
        pass # TODO: Complete this test.

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()