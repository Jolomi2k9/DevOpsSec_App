import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestApp(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome WebDriver using ChromeDriverManager
        options = Options()
        options.headless = True  # Run in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_title(self):
        # Define the expected title of the page
        expected_title = "Volunteer app"
        # Navigate to the application URL
        self.driver.get("http://127.0.0.1:5000")
        # Assert that the title is as expected
        self.assertIn(expected_title, self.driver.title)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

