import pdb
import unittest
from random import randrange
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

class TestWebPage(unittest.TestCase):

    driver = None
    selectors = {
        'articles': """//*[@id="firehoselist"]/article[@data-fhid]""",
        'icons': """//*[@id="firehoselist"]/article[@data-fhid]/header/span/a/img""",
        'polls': """//a[@href="//slashdot.org/polls"]""",
        'answers': """//form[@id="pollBooth"]/label""",
        'vote': """//button[@type="submit"][@class="btn-polls"]""",
        'numbers_of_votes': """//div[@class="poll-bar-text"]""",
    }

    def setUp(self):
        path_to_binary = '/Users/ccelis/django/ecobee/test_2/chromedriver'
        self.driver = webdriver.Chrome(path_to_binary)

    def wait(self, driver, xpath_selector):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_selector))
        )

    def click_element(self,driver, xpath_selector):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_selector))
        ).click()

    def visit_web_page(self,driver,web_page='http://slashdot.org/'):
        driver.get(web_page)
        self.wait(driver, self.selectors['articles'])

    def test_count_articles(self):
        '''
        Print how many articles are on the page
        '''
        driver = self.driver
        selectors = self.selectors
        self.visit_web_page(driver)
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
        self.visit_web_page(driver)
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
        Return the number of people that have voted for that same option
        '''
        driver = self.driver
        selectors = self.selectors
        self.visit_web_page(driver)
        self.click_element(driver, selectors['polls'])
        self.wait(driver, selectors['answers'])
        answers = driver.find_elements_by_xpath(selectors['answers'])
        number_of_answers = len(answers)
        selected_answer = randrange(number_of_answers)
        answers[selected_answer].click()
        # selected_answer
        # 0 => Yes
        # 1 => No
        # 2 => Depends
        self.click_element(driver, selectors['vote'])
        self.wait(driver, selectors['numbers_of_votes'])
        numbers_of_votes = driver.find_elements_by_xpath(selectors['numbers_of_votes'])
        result = numbers_of_votes[selected_answer].text.split('/')[0].split(' ')[0]
        print(result)
        return result

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()