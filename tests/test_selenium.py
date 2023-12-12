import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestApp(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver with the desired options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")  # Crucial for Jenkins or Docker environments
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        options.add_argument("--disable-gpu")  # GPU not used in headless mode
        options.add_argument("--disable-extensions")  # Disable any browser extensions during the test
        options.add_argument("--disable-infobars")  # Prevent infobars from appearing
        
        # Initialize Chrome WebDriver using ChromeDriverManager
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


