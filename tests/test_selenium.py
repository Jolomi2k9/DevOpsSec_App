import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    #test if navbar titles are as expected
    def test_title(self):        
        # go to the application URL
        self.driver.get("http://127.0.0.1:5000")
        # Wait for page to load and check if links work by clicking on it 
        about_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "About"))
        )
        about_link.click()
        # Wait for the page to load and check if title correct
        expected_title = "About"
        self.assertIn(expected_title, self.driver.title)
    #test to verify if links in the navbar works
    def test_navbar_links(self):
        # go to the application URL
        self.driver.get("http://127.0.0.1:5000")
        # wait for page to load
        links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav .navbar-nav li a"))
        )
        #loop through nav bar links and click
        for link in links:
            href = link.get_attribute("href")
            # wait for page to load
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(link)).click()
            self.assertEqual(self.driver.current_url, href)
            self.driver.back()


    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


