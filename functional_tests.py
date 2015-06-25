import unittest

from selenium import webdriver

class InitialPageLoadTests(unittest.TestCase):
    START_PAGE_URL = 'file:///home/tdpreece/javascript_projects/pacman_javascript_qunit_requirejs/index.html'

    def test_title_of_page_is_pacman(self):
        browser = webdriver.PhantomJS()
        browser.get(self.START_PAGE_URL)
        self.assertIn('PacMan', browser.title)

