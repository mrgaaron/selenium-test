from selenium.webdriver.common.by import By


class BasePage(object):
    """Describes elements and functionality in common on all Uptake site pages"""

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, page):
        navbar_item = self.driver.find_element(By.LINK_TEXT, page)
        navbar_item.click()
