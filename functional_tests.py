import unittest

from selenium import webdriver

class InitialPageLoadTests(unittest.TestCase):
    def test_title_of_page_is_pacman(self):
        browser = webdriver.PhantomJS()
        browser.get('file:///home/tdpreece/javascript_projects/pacman_javascript_qunit_requirejs/index.html')
        self.assertIn('PacMan', browser.title)

