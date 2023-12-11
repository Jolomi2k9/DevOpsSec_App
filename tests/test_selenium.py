from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import os


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # Print the current working directory before setting up the Chrome webdriver
        print("Current working directory before webdriver setup:", os.getcwd())

        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')  
        options.add_argument('--disable-gpu')  
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--no-first-run')
        options.add_argument('--disable-extensions')
        options.add_argument('--verbose')
        options.add_argument('--log-path=/home/ubuntu/jenkins/workspace/voluntApp-multibranch_main/chromedriver.log')

        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

  
        # Using webdriver_manager to manage the driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

         # Print the current working directory after setting up the Chrome webdriver
        print("Current working directory after webdriver setup:", os.getcwd())

    def test_title(self):        
        expected_title = "Volunteer app"
        self.driver.get("http://127.0.0.1:5000")
        self.assertIn(expected_title, self.driver.title)

    def tearDown(self):
        # stop the driver after the test suite is completed.
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

