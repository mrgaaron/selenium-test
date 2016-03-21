from selenium.webdriver.common.by import By
from base import BasePage


class HomePage(BasePage):
    """Verifications for the Uptake home page"""

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def has_title_match(self):
        """Asserts the title of the page is what we expect"""

        # can't just test for "Uptake" because that's in all the page titles
        return "Analytics for the Industrial Internet" in self.driver.title

    def is_navbar_in_correct_state(self):
        """Asserts that no navbar elements are "highlighted" as they would be on a subpage"""

        navbar_items = self.driver.find_elements(By.CSS_SELECTOR, "li.current-menu-item")
        return len(navbar_items) == 0
