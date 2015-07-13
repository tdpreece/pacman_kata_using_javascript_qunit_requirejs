import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class InitialPageLoadTests(unittest.TestCase):
    START_PAGE_URL = (
        'file:///home/tdpreece/javascript_projects/'
        'pacman_javascript_qunit_requirejs/index.html'
    )

    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def assert_element_with_id_exists(self, id):
        elements = self.browser.find_elements(By.ID, id)
        number_of_elements = len(elements)
        self.assertEqual(
            number_of_elements,
            1,
            "One element with id='{id}' expected, {number_of_elements} found."
            .format(id=id, number_of_elements=number_of_elements)
        )

    def test_title_of_page_is_pacman(self):
        self.browser.get(self.START_PAGE_URL)
        self.assertIn('PacMan', self.browser.title)

    def test_pacman_is_on_page(self):
        self.browser = webdriver.PhantomJS()
        self.browser.get(self.START_PAGE_URL)
        self.assert_element_with_id_exists('pacman')
