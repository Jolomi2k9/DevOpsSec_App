import unittest
import xmlrunner
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
        # Set up the Chrome WebDriver 
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")  
        options.add_argument("--disable-dev-shm-usage")  
        options.add_argument("--disable-gpu")  
        options.add_argument("--disable-extensions")  
        options.add_argument("--disable-infobars")  
        
        # Initialize Chrome WebDriver using ChromeDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # def scroll_to_element_and_click(self, element):
    #     # scroll to view element
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)        
    #     # Re-locate element 
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(element)
    #     )        
    #     # Use javaScript to click 
    #     self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element_and_click(self, element_locator):
        # Wait for the element to be clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(element_locator)
        )
        # Scroll to the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Use JavaScript to click on the element
        self.driver.execute_script("arguments[0].click();", element)


    def test_about_link(self):
        # go to the application URL
        self.driver.get("http://127.0.0.1:5000")
        # Find about link and click it
        about_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "About"))
        )
        self.scroll_to_element_and_click(about_link)
        # Wait for the page to load and check if URL is correct
        expected_url = "http://127.0.0.1:5000/about"  # Update this based on your actual URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url)
        )
        self.assertEqual(self.driver.current_url, expected_url)

    # def test_logo_is_displayed(self):
    #     # Go to the application URL
    #     self.driver.get("http://127.0.0.1:5000")

    #     # Wait for the logo to be visible
    #     logo = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand img"))
    #     )

    #     # Assert that the logo is displayed
    #     self.assertTrue(logo.is_displayed(), "Logo is not displayed on the page")

    def test_logo_is_displayed(self):
        # Go to the application URL
        self.driver.get("http://127.0.0.1:5000")

        # Wait for the logo to be visible
        logo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/static/images/logo.png']"))
        )

        # Assert that the logo is displayed
        self.assertTrue(logo.is_displayed(), "Logo is not displayed on the page")





    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

   



