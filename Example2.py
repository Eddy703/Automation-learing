############################################################################
#I do not own the code written in this file,                               #
#The following code is a direct copy off from                              #
#https://selenium-python.readthedocs.io/getting-started.html#simple-usage  #
#This is just to mark down some important points for myself                #
############################################################################

import unittest
#Module used for testing certain things such as
#self.assertEqual('foo'.upper(),'FOO') assertTrue False and such
#More on the python official documentation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Keys class provide keyboard input

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
