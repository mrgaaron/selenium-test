from selenium.webdriver.common.by import By
from base import BasePage


class PeoplePage(BasePage):
    """Verifications and functions for the "People" page on the Uptake site"""

    def __init__(self, driver):
        super(PeoplePage, self).__init__(driver)

    def has_title_match(self):
        """Asserts the title of the page is what we expect"""

        # can't just test for "Uptake" because that's in all the page titles
        return "People" in self.driver.title

    def is_navbar_in_correct_state(self):
        """Asserts that the People navbar element is "highlighted" """

        navbar_item = self.driver.find_element(By.CSS_SELECTOR, "li.current-menu-item")
        return navbar_item.text == "People"
