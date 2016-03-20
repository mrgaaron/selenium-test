import unittest
from selenium import webdriver
from page import HomePage, PeoplePage


class UptakeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_navigation_from_home_to_people(self):
        self.driver.get('http://www.uptake.com')
        home = HomePage(self.driver)
        self.assertTrue(home.has_title_match())
        self.assertTrue(home.navbar_in_correct_state())

        home.navigate("People")

        people = PeoplePage(self.driver)
        self.assertTrue(people.has_title_match())
        self.assertTrue(people.navbar_in_correct_state())