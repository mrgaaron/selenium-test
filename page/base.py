from selenium.webdriver.common.by import By


class BasePage(object):
    """Describes elements and functionality in common on all Uptake site pages"""

    def __init__(self, driver):
        self.driver = driver

    def click_navbar_link(self, page_name):
        """Navigate to the given `page` specified by the link name in the top navbar"""

        navbar_item = self.driver.find_element(By.LINK_TEXT, page_name)
        navbar_item.click()
