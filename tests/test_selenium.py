from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class ExampleComTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver instance
        # Make sure the 'chromedriver' executable is in your PATH or provide the path to the executable.
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

    def test_title(self):
        # Replace 'Example Domain' with the actual expected title of your Flask application's index page.
        expected_title = "Your Expected Title Here"
        self.driver.get("http://127.0.0.1:5000")
        self.assertIn(expected_title, self.driver.title)

    def tearDown(self):
        # Quit the driver after the test suite is completed.
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

