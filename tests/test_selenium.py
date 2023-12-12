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
    # def test_title(self):        
    #     # go to the application URL
    #     self.driver.get("http://127.0.0.1:5000")
    #     # Wait for page to load and check if links work by clicking on it 
    #     about_link = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.LINK_TEXT, "About"))
    #     )
    #     about_link.click()
    #     # Wait for the page to load and check if title correct
    #     expected_title = "About"
    #     self.assertIn(expected_title, self.driver.title)
    # #test to verify if links in the navbar works
    # def test_navbar_links(self):
    #     # go to the application URL
    #     self.driver.get("http://127.0.0.1:5000")
    #     # wait for page to load
    #     links = WebDriverWait(self.driver, 160).until(
    #         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav .navbar-nav li a"))
    #     )
    #     #loop through nav bar links and click
    #     for link in links:
    #         href = link.get_attribute("href")
    #         # wait for page to load
    #         WebDriverWait(self.driver, 160).until(EC.element_to_be_clickable(link)).click()
    #         self.assertEqual(self.driver.current_url, href)
    #         self.driver.back()

    # def scroll_to_element_and_click(self, element):
    #     # Scroll element into view
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     # Wait for element to be clickable
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(element))
    #     # Use JavaScript to click on the element
    #     self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element_and_click(self, element):
        # Scroll element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        # Re-locate the element after scrolling
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(element)
        )
        
        # Use JavaScript to click on the element
        self.driver.execute_script("arguments[0].click();", element)

    def test_about_link(self):
        # go to the application URL
        self.driver.get("http://127.0.0.1:5000")
        # Find the 'About' link and click it
        about_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "About"))
        )
        self.scroll_to_element_and_click(about_link)
        about_link.click()
        # Wait for the page to load and check if URL is correct
        expected_url = "http://127.0.0.1:5000/about"  # Update this based on your actual URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url)
        )
        self.assertEqual(self.driver.current_url, expected_url)

    def test_join_link(self):
        # go to the application URL
        self.driver.get("http://127.0.0.1:5000")
        # Find the 'Join' link and click it
        join_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Join"))
        )
        self.scroll_to_element_and_click(join_link)
        join_link.click()
        # Wait for the page to load and check if URL is correct
        expected_url = "http://127.0.0.1:5000/join"  # Update this based on your actual URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url)
        )
        self.assertEqual(self.driver.current_url, expected_url)



    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


