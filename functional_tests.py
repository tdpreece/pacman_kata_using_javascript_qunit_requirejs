import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InitialPageLoadTests(unittest.TestCase):
    IMPLICIT_WAIT_TIME = 2

    START_PAGE_URL = (
        'file:///home/tdpreece/javascript_projects/'
        'pacman_javascript_qunit_requirejs/index.html'
    )

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        # self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(self.IMPLICIT_WAIT_TIME)

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

    def test_pacman_is_on_gameboard(self):
        self.browser.get(self.START_PAGE_URL)
        self.browser.find_element_by_css_selector('#pacman')
        # self.browser.find_element(By.css_selector('#pacman'))
        self.assert_element_with_id_exists('pacman')


class PacmanMovementTests(unittest.TestCase):
    IMPLICIT_WAIT_TIME = 2
    START_PAGE_URL = (
        'file:///home/tdpreece/javascript_projects/'
        'pacman_javascript_qunit_requirejs/index.html'
    )

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)
        self.browser.implicitly_wait(self.IMPLICIT_WAIT_TIME)

    def test_pacman_moves_left_on_left_button_click(self):
        self.browser.get(self.START_PAGE_URL)
        pacman_start = self.browser.find_element_by_id('pacman')
        x_start = pacman_start.location['x']
        y_start = pacman_start.location['y']
        body = self.browser.find_element_by_css_selector('body')
        body.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
        pacman_finish = self.browser.find_element_by_id('pacman')
        x_finish = pacman_finish.location['x']
        y_finish = pacman_finish.location['y']
        self.assertTrue(
            x_start > x_finish,
            "x_start={0}, x_finish={1}".format(x_start, x_finish)
        )
        self.assertEqual(y_start, y_finish)

    def test_pacman_moves_right_on_right_button_click(self):
        self.browser.get(self.START_PAGE_URL)
        pacman_start = self.browser.find_element_by_id('pacman')
        x_start = pacman_start.location['x']
        y_start = pacman_start.location['y']
        body = self.browser.find_element_by_css_selector('body')
        body.send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)
        pacman_finish = self.browser.find_element_by_id('pacman')
        x_finish = pacman_finish.location['x']
        y_finish = pacman_finish.location['y']
        self.assertTrue(
            x_start < x_finish,
            "x_start={0}, x_finish={1}".format(x_start, x_finish)
        )
        self.assertEqual(y_start, y_finish)

    def test_pacman_moves_right_and_then_left(self):
        self.browser.get(self.START_PAGE_URL)
        pacman_start = self.browser.find_element_by_id('pacman')
        x_start = pacman_start.location['x']
        y_start = pacman_start.location['y']
        body = self.browser.find_element_by_css_selector('body')
        body.send_keys(Keys.ARROW_RIGHT)
        body.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
        pacman_finish = self.browser.find_element_by_id('pacman')
        x_finish = pacman_finish.location['x']
        y_finish = pacman_finish.location['y']
        self.assertEqual(
            x_start, x_finish,
            "x_start={0}, x_finish={1}".format(x_start, x_finish)
        )
        self.assertEqual(y_start, y_finish)
