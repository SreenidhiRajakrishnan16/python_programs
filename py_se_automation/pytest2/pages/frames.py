from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

class Frames:

    def __init__(self, driver):
        self.driver = driver
    
    def navigate_frames(self):
        # driver = Chrome()
        self.driver.switch_to.frame('courses-iframe')
        link = self.driver.find_element(By.XPATH, "//a[@class='header-top-link']").get_attribute('href')
        print(link)